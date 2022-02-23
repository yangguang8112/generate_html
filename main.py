#!coding=utf-8
"""
Created by Guang Yang
You can contact the developer via yangguang2@genomics.cn or access the details via https://github.com/yangguang8112/generate_html.git
"""

from types import resolve_bases
from jinja2 import Template
import sys
import json
from config import Config
import os
import time
import pandas as pd
from merge_fig import *

# template_file = sys.argv[1]
# data_json_file = sys.argv[2]
# out_html_file = sys.argv[3]

def generate_content(template_file, data_json, out_html_file):
    with open(template_file, 'r') as tf:
        template_html = tf.read()
    # with open(data_json_file, 'r') as djf:
    #     data = json.loads(djf.read())
    html = Template(template_html)
    res_html = html.render(data_json)

    with open(out_html_file, 'w') as oht:
        oht.write(res_html)

def merge_html(base_html_name, content_html_name, out_html_name):
    CONTENT_LINE_NUM = 6376
    # base_html_name = 'split_base.html'
    # content_html_name = 'split_content.html'
    # out_html_name = 'report.html'

    base_html = open(base_html_name, 'r').readlines()
    content_html = open(content_html_name, 'r').read()

    with open(out_html_name, 'w') as ohe:
        for line in base_html[:CONTENT_LINE_NUM]:
            ohe.write(line)
        ohe.write(content_html)
        for line in base_html[CONTENT_LINE_NUM:]:
            ohe.write(line)

def is_float(var):
    if not var.isdigit():
        try:
            return str(round(float(var), 3))
        except:
            return var
    return var


def generate_data(result_path, config):
    old_json = result_path + '/Backup/final_parameter.json'
    with open(old_json, 'r') as oj:
        old_res = json.loads(oj.read())
    res = {}
    res['date'] = time.strftime("%d %b %Y", time.localtime())
    # summary data from old json
    res['summary'] = {'species': old_res['Species']}
    res['summary']['title'] = old_res['Project_id']
    res['summary']['TCR'] = {"has": old_res['TCR']}
    res['summary']['BCR'] = {"has": old_res['BCR']}
    res['summary']['others'] = old_res
    res['summary']['RNA'] = old_res['RNA']
    # 
    # df = pd.read_csv(result_path+"/"+config.need_result_table_file_list[0], header=0, sep='\t', thousands=',')
    # sample_num  = len(df)
    # res['summary']['sample_num'] = str(sample_num)
    # res['summary']['cell_num_per_sample'] = str(round(df['Estimated Number of Cells'].mean(), 2))
    # res['summary']['cell_num'] = str(df['Estimated Number of Cells'].sum())
    # res['summary']['map_rate_ave_sample'] = str(round(sum([float(i.strip("%")) for i in df['Reads Mapped to Genome']]) / sample_num, 2)) + '%'
    # #
    # df = pd.read_csv(result_path+"/"+config.need_result_table_file_list[1], header=0, sep='\t', thousands=',')
    # res['summary']['filtered_cell_num'] = str(df['Final_cells_number'].sum())
    # res['summary']['filtered_cell_num_per_sample'] = str(round(df['Final_cells_number'].mean(), 2))
    # table data
    immune_types = []
    if old_res['TCR']:
        immune_types.append('TCR')
        res['TCR'] = {}
    if old_res['BCR']:
        immune_types.append('BCR')
        res['BCR'] = {}
    for immune_type in immune_types:
        for table_name, data_file in zip(config.data_json_keys, config.need_result_table_file_list[immune_type]):
            res[immune_type][table_name] = {"header": [], "data": []}
            df = pd.read_csv(result_path + '/' + data_file, header=0, sep='\t', thousands=',')
            res[immune_type][table_name]["header"] = df.columns.tolist()
            for i in range(min(10, len(df))):
                line = df.iloc[i]
                res[immune_type][table_name]["data"].append([str(i) for i in line.values.tolist()])
            if table_name == config.data_json_keys[0]:
                res['summary'][immune_type]['sample_num'] = str(len(df))
                res['summary'][immune_type]['raw_cell_num'] = str(df['Estimated Number of Cells'].sum())
                res['summary'][immune_type]['filted_VJ_cell_num'] = str(df['Number of Cells With Productive V-J Spanning Pair'].sum())
                res['summary'][immune_type]['raw_cell_num_per_sample'] = str(round(df['Estimated Number of Cells'].mean(), 2))
                res['summary'][immune_type]['filted_VJ_cell_num_per_sample'] = str(round(df['Number of Cells With Productive V-J Spanning Pair'].mean(), 2))
                res['summary'][immune_type]['map_vdj_rate'] = format(((df['Number of Read Pairs'] * df['Reads Mapped to Any V(D)J Gene'].str.strip("%").astype(float)/100) / df['Number of Read Pairs'].sum() * 100).sum(), '.2f') + '%'
    res['summary']['immune_types'] = immune_types
    res['table_keys'] = config.data_json_keys
        
    # for table_name, data_file in zip(config.data_json_keys, config.need_result_table_file_list):
    #     res[table_name] = {"data": []}
    #     try:
    #         # 处理没有结果的情况
    #         df = pd.read_csv(result_path + '/' + data_file, header=0, sep='\t')
    #     except:
    #         break
    #     # max line == 8
    #     for i in range(min(8, len(df))):
    #         line = df.iloc[i]
    #         # res[table_name]["data"].append([is_float(str(i)) for i in line.values.tolist()])
    #         res[table_name]["data"].append([str(i) for i in line.values.tolist()])
    #     # gene list too long
    #     if table_name in ['cluster0_Biological_Process_enrich_list', 'cluster0_KEGG_pathway_enrich_list']:
    #         for data in res[table_name]["data"]:
    #             data[-2] = data[-2][:8] + '...'

    # final_cluster_stat need colname
    # df = pd.read_csv(result_path + '/' + config.need_result_table_file_list[config.data_json_keys.index('final_cluster_stat')], header=0, sep='\t')
    # res['final_cluster_stat']['samples'] = df.columns.tolist()[1:]
    # # table 4 FC 小数位
    # for l in res['diffCluster_stat']['data']:
    #     l[2] = is_float(l[2])
    #
    return res

def get_abs_path(file_list, path):
    return [path + '/' + i.split("/")[-1] for i in file_list]


def main():
    result_path = sys.argv[1]
    if len(sys.argv) == 3:
        report_path = sys.argv[2]
        if not os.path.exists(report_path):
            os.mkdir(report_path)
    else:
        report_path = result_path + '/report'
        if not os.path.exists(report_path):
            os.mkdir(report_path)
        else:
            os.system("rm -rf " + report_path)
            os.mkdir(report_path)

    config = Config()
    if not os.path.exists(result_path):
        print("Not Found result data")
        exit()
    
    # cp result and template file
    main_path = os.path.split(os.path.realpath(__file__))[0]
    # get_data_json
    data_json = generate_data(result_path, config)
    # print(main_path)
    os.system("cp -r {main_path}/Template/full_size_page {report_path};cp -r {main_path}/Template/report_files {report_path}".format(report_path=report_path, main_path=main_path))
    os.mkdir("{report_path}/result_file".format(report_path=report_path))
    os.mkdir("{report_path}/show_img".format(report_path=report_path))
    os.mkdir("{report_path}/img".format(report_path=report_path))
    # sample name file
    for immune_type in data_json['summary']['immune_types']:
        # eg_sample1 = data_json[immune_type + '_summary']['data'][0][0][:-2]
        # ################################################### gai 1111111111111111111111111111
        # eg_sample2 = data_json[immune_type + '_summary']['data'][1][0][:-2]
        eg_sample1 = data_json['summary']['others']['fig5_'+immune_type+'_sample1']
        eg_sample2 = data_json['summary']['others']['fig5_'+immune_type+'_sample2']
        for index, fn in enumerate(config.need_result_fig_file_list['fig4'][immune_type][:3]):
            tmp = fn.split("/")
            tmp[-1] = eg_sample1 + '.' + tmp[-1].split(".")[-1]
            config.need_result_fig_file_list['fig4'][immune_type][index] = "/".join(tmp)
        config.need_result_fig_file_list['fig5'][immune_type][0] = config.need_result_fig_file_list['fig5'][immune_type][0].split("aa_from_")[0] + "aa_from_" + eg_sample1 + '.png'
        config.need_result_fig_file_list['fig5'][immune_type][1] = config.need_result_fig_file_list['fig5'][immune_type][1].split("aa_from_")[0] + "aa_from_" + eg_sample2 + '.png'
    # print(config.need_result_fig_file_list['fig4'])

    # TODO cp result file
    for immune_type in data_json['summary']['immune_types']:
        for file in config.need_result_table_file_list[immune_type]:
            os.system("cp {result_path}/{file} {report_path}/result_file".format(result_path=result_path, report_path=report_path, file=file))
        # for files in config.need_result_fig_file_list.values():
        #     for f in files[immune_type]:
        #         os.system("cp {result_path}/{f} {report_path}/result_file".format(result_path=result_path, f=f, report_path=report_path))
        for index, file in enumerate(config.need_result_fig_file_list['fig4'][immune_type][:3]):
            tmp = file.split("/")
            new_name = immune_type + '-' + tmp[-2] + '-' + tmp[-1]
            os.system("cp {result_path}/{file} {report_path}/result_file/{new_name}".format(result_path=result_path, report_path=report_path, file=file, new_name=new_name))
            tmp[-1] = new_name
            config.need_result_fig_file_list['fig4'][immune_type][index] = "/".join(tmp)
        for i in [1,2,3,5,6,7]:
            if i == 7 and data_json['summary']['RNA'] == 0:
                continue
            fig_name = 'fig' + str(i)
            for index, file in enumerate(config.need_result_fig_file_list[fig_name][immune_type]):
                new_name = immune_type + '-' + file.split("/")[-1]
                os.system("cp {result_path}/{file} {report_path}/result_file/{new_name}".format(result_path=result_path, report_path=report_path, file=file, new_name=new_name))
                config.need_result_fig_file_list[fig_name][immune_type][index] = new_name

    
    # generate show image
    for image_index in range(1, 8):
        if i == 7 and data_json['summary']['RNA'] == 0:
            continue
        fig_name = 'fig' + str(image_index)
        try:
            for immune_type in data_json['summary']['immune_types']:
                file_name = immune_type + '_' + fig_name + '.png'
                file_num = len(config.need_result_fig_file_list[fig_name][immune_type])
                concat_images(get_abs_path(config.need_result_fig_file_list[fig_name][immune_type], report_path + '/result_file'), report_path+'/show_img/'+ file_name, 2, file_num // 2, text_size=20)
        except:
            config.check_sec['cell_filter'] = 0
    data_json['check_sec'] = config.check_sec
    # generate report html
    generate_content(main_path + "/Template/split_content_temp.html", data_json, report_path + "/tmp.html")
    for i in range(1, 8):
        if i == 7 and data_json['summary']['RNA'] == 0:
            continue
        fig_html_name = 'Fig' + str(i) + '.html'
        generate_content(main_path + "/Template/full_size_page/" + fig_html_name, data_json, report_path + "/full_size_page/" + fig_html_name)
    merge_html(main_path + "/Template/split_base.html", report_path + "/tmp.html", report_path + "/report.html")
    os.system("rm {report_path}/tmp.html".format(report_path=report_path))




if __name__ == "__main__":
    # resul = "/home/yangguang/work/scRNA_report/Result"
    main()

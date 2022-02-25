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
    old_json = result_path + '/../Backup/02_JSON/final_parameter.json'
    with open(old_json, 'r') as oj:
        old_res = json.loads(oj.read())
    res = {}
    res['date'] = time.strftime("%d %b %Y", time.localtime())
    # summary data from old json
    res['summary'] = {'species': old_res['Species']}
    res['summary']['title'] = old_res['project_id']
    res['summary']['choose_resulotion'] = old_res['choose_res']
    res['summary']['FC'] = old_res['FC']
    res['summary']['pvalue'] = old_res['pvalue']
    res['summary']['mincell'] = old_res['mincell']
    res['summary']['res_value'] = old_res
    if old_res['FDR'] != 'NULL':
        res['summary']['thred_desc'] = ' & FDR ≤ ' + old_res['FDR']
    else:
        if old_res['pvalue'] != 'NULL':
            res['summary']['thred_desc'] = ' & P-value ≤ ' + old_res['pvalue']
        else:
            res['summary']['thred_desc'] = ''
        
    # 
    df = pd.read_csv(result_path+"/"+config.need_result_table_file_list[0], header=0, sep='\t', thousands=',')
    sample_num  = len(df)
    res['summary']['sample_num'] = str(sample_num)
    res['summary']['cell_num_per_sample'] = str(round(df['Estimated Number of Cells'].mean(), 2))
    res['summary']['cell_num'] = str(df['Estimated Number of Cells'].sum())
    res['summary']['map_rate_ave_sample'] = str(round(sum([float(i.strip("%")) for i in df['Reads Mapped to Genome']]) / sample_num, 2)) + '%'
    #
    df = pd.read_csv(result_path+"/"+config.need_result_table_file_list[1], header=0, sep='\t', thousands=',')
    res['summary']['filtered_cell_num'] = str(df['Final_cells_number'].sum())
    res['summary']['filtered_cell_num_per_sample'] = str(round(df['Final_cells_number'].mean(), 2))
    # table data
    for table_name, data_file in zip(config.data_json_keys, config.need_result_table_file_list):
        res[table_name] = {"data": [], "header": []}
        try:
            # 处理没有结果的情况
            df = pd.read_csv(result_path + '/' + data_file, header=0, sep='\t')
        except:
            break
        # max line == 8
        res[table_name]["header"] = df.columns.tolist()
        for i in range(min(8, len(df))):
            line = df.iloc[i]
            # res[table_name]["data"].append([is_float(str(i)) for i in line.values.tolist()])
            res[table_name]["data"].append([str(i) for i in line.values.tolist()])
        # gene list too long
        if table_name in ['cluster0_Biological_Process_enrich_list', 'cluster0_KEGG_pathway_enrich_list']:
            for data in res[table_name]["data"]:
                data[-2] = data[-2][:8] + '...'
    # final_cluster_stat need colname
    df = pd.read_csv(result_path + '/' + config.need_result_table_file_list[config.data_json_keys.index('final_cluster_stat')], header=0, sep='\t')
    res['final_cluster_stat']['samples'] = df.columns.tolist()[1:]
    # table 4 FC 小数位
    for l in res['diffCluster_stat']['data']:
        l[2] = is_float(l[2])
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
    config.need_result_fig_file_list['fig3'][1] = config.need_result_fig_file_list['fig3'][1].replace("_uniqstr_", data_json['summary']['res_value']['topGene_Show'])
    config.need_result_fig_file_list['fig3'][3] = config.need_result_fig_file_list['fig3'][3].replace("_uniqstr_", data_json['summary']['res_value']['topGene_Show'])
    # print(main_path)
    os.system("cp -r {main_path}/Template/full_size_page {report_path};cp -r {main_path}/Template/report_files {report_path}".format(report_path=report_path, main_path=main_path))
    os.mkdir("{report_path}/result_file".format(report_path=report_path))
    os.mkdir("{report_path}/show_img".format(report_path=report_path))
    # os.mkdir("{report_path}/img".format(report_path=report_path))
    # TODO cp result file
    os.system("cp -r {result_path}/Result_2_Analysis/03_Difference/diffCluster_File {report_path}/result_file".format(result_path=result_path, report_path=report_path))
    for index, file in enumerate(config.need_result_table_file_list):
        # index 和 文件 和html中的sec对应起来
        os.system("cp {result_path}/{file} {report_path}/result_file".format(result_path=result_path, report_path=report_path, file=file))
    # 图片“详见”拷贝
    # os.system("cp {result_path}/Result_2_Analysis/03_Difference/diffCluster_volcano/All.*.volcano.png {report_path}/img".format(result_path=result_path, report_path=report_path))
    # os.system("cp {result_path}/Result_2_Analysis/03_Difference/diffCluster_picture/All.*marker*.png {report_path}/img".format(result_path=result_path, report_path=report_path))
    for files in config.need_result_fig_file_list.values():
        for f in files:
            os.system("cp {result_path}/{f} {report_path}/result_file".format(result_path=result_path, f=f, report_path=report_path))
    
    # generate show image
    try:
        merge_fig1(get_abs_path(config.need_result_fig_file_list['fig1'], report_path + '/result_file'), report_path+'/show_img')
    except KeyError as e:
        print("fig1 merge error!!!!!!!!")
        print(e)
        config.check_sec['cell_filter'] = 0
    try:
        merge_fig2(get_abs_path(config.need_result_fig_file_list['fig2'], report_path + '/result_file'), report_path+'/show_img')
    except KeyError as e:
        print("fig2 merge error!!!!!!!!")
        print(e)
        config.check_sec['sample_merge'] = 0
    try:
        merge_fig3_new_new(get_abs_path(config.need_result_fig_file_list['fig3'], report_path + '/result_file'), report_path+'/show_img')
    except KeyError as e:
        print("fig3 merge error!!!!!!!!")
        print(e)
        config.check_sec['cell_cluster_marker'] = 0
    try:
        merge_fig4(get_abs_path(config.need_result_fig_file_list['fig4'], report_path + '/result_file'), report_path+'/show_img')
    except KeyError as e:
        print("fig4 merge error!!!!!!!!")
        print(e)
        config.check_sec['go_kegg'] = 0
    try:
        merge_fig5(get_abs_path(config.need_result_fig_file_list['fig5'], report_path + '/result_file'), report_path+'/show_img')
    except KeyError as e:
        print("fig5 merge error!!!!!!!!")
        print(e)
        config.check_sec['pseudotime'] = 0
    try:
        merge_fig6(get_abs_path(config.need_result_fig_file_list['fig6'], report_path + '/result_file'), report_path+'/show_img')
    except KeyError as e:
        print("fig6 merge error!!!!!!!!")
        print(e)
        config.check_sec['cell_type'] = 0
    data_json['check_sec'] = config.check_sec
    # generate report html
    generate_content(main_path + "/Template/split_content_temp.html", data_json, report_path + "/tmp.html")
    merge_html(main_path + "/Template/split_base.html", report_path + "/tmp.html", report_path + "/report.html")
    os.system("rm {report_path}/tmp.html".format(report_path=report_path))
    os.system("rm -rf {report_path}/result_file/".format(report_path=report_path))




if __name__ == "__main__":
    # resul = "/home/yangguang/work/scRNA_report/Result"
    main()

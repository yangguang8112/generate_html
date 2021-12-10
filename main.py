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

def generate_data(result_path, config):
    res = {}
    res['date'] = time.strftime("%d %b %Y", time.localtime())
    # species need var
    res['summary'] = {'species': "human"}
    df = pd.read_csv(result_path+"/"+config.need_result_table_file_list[0], header=0, sep='\t', thousands=',')
    sample_num  = len(df)
    res['summary']['sample_num'] = str(sample_num)
    res['summary']['cell_num_per_sample'] = str(df['Estimated Number of Cells'].mean())
    res['summary']['cell_num'] = str(df['Estimated Number of Cells'].sum())
    res['summary']['map_rate_ave_sample'] = str(sum([float(i.strip("%")) for i in df['Reads Mapped to Genome']]) / sample_num) + '%'
    # table data
    for table_name, data_file in zip(config.data_json_keys, config.need_result_table_file_list):
        res[table_name] = {"data": []}
        df = pd.read_csv(result_path + '/' + data_file, header=0, sep='\t')
        # max line == 8
        for i in range(min(8, len(df))):
            line = df.iloc[i]
            res[table_name]["data"].append([str(i) for i in line.values.tolist()])
    # final_cluster_stat need colname
    df = pd.read_csv(result_path + '/' + config.need_result_table_file_list[config.data_json_keys.index('final_cluster_stat')], header=0, sep='\t')
    res['final_cluster_stat']['samples'] = df.columns.tolist()[1:]
    return res

def get_abs_path(file_list, path):
    return [path + '/' + i.split("/")[-1] for i in file_list]


def main():
    result_path = sys.argv[1]
    report_path = sys.argv[2]
    config = Config()
    if not os.path.exists(result_path):
        print("Not Found result data")
        exit()
    if not os.path.exists(report_path):
        os.mkdir(report_path)
    # cp result and template file
    os.system("cp -r Template/full_size_page {report_path};cp -r Template/report_files {report_path}".format(report_path=report_path))
    os.mkdir("{report_path}/result_file".format(report_path=report_path))
    os.mkdir("{report_path}/show_img".format(report_path=report_path))
    # TODO cp result file
    os.system("cp -r {result_path}/Result_2_Analysis/03_Difference/diffCluster_File {report_path}/result_file".format(result_path=result_path, report_path=report_path))
    for file in config.need_result_table_file_list:
        os.system("cp {result_path}/{file} {report_path}/result_file".format(result_path=result_path, report_path=report_path, file=file))
    # pic 还差在fig.html里面的一些图片“详见”链接没有处理
    for files in config.need_result_fig_file_list.values():
        for f in files:
            os.system("cp {result_path}/{f} {report_path}/result_file".format(result_path=result_path, f=f, report_path=report_path))
    # get_data_json
    data_json = generate_data(result_path, config)
    # generate show image
    merge_fig1(get_abs_path(config.need_result_fig_file_list['fig1'], report_path + '/result_file'), report_path+'/show_img')
    merge_fig2(get_abs_path(config.need_result_fig_file_list['fig2'], report_path + '/result_file'), report_path+'/show_img')
    merge_fig3(get_abs_path(config.need_result_fig_file_list['fig3'], report_path + '/result_file'), report_path+'/show_img')
    merge_fig4(get_abs_path(config.need_result_fig_file_list['fig4'], report_path + '/result_file'), report_path+'/show_img')
    merge_fig5(get_abs_path(config.need_result_fig_file_list['fig5'], report_path + '/result_file'), report_path+'/show_img')
    merge_fig6(get_abs_path(config.need_result_fig_file_list['fig6'], report_path + '/result_file'), report_path+'/show_img')
    # generate report html
    generate_content("Template/split_content_temp.html", data_json, report_path + "/tmp.html")
    merge_html("Template/split_base.html", report_path + "/tmp.html", report_path + "/report.html")
    os.system("rm {report_path}/tmp.html".format(report_path=report_path))




if __name__ == "__main__":
    # resul = "/home/yangguang/work/scRNA_report/Result"
    main()

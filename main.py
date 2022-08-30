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

def process_table_file(file_path, head_row_num=None):
    df = pd.read_table(file_path)
    if head_row_num:
        df = df.iloc[:head_row_num]
    header = df.columns.tolist()
    data = []
    for i in range(df.shape[0]):
        line = df.iloc[i]
        data.append([str(i) for i in line.values.tolist()])
    return {"header": header, "data": data}


def generate_data(result_path, config):
    old_json = result_path + '/config/final_parameter.json'
    with open(old_json, 'r') as oj:
        old_res = json.loads(oj.read())
    res = {}
    res['date'] = time.strftime("%d %b %Y", time.localtime())
    # summary data from old json
    res['summary'] = {'species': old_res['Species']}
    res['summary']['title'] = old_res['Project_id']
    for k, v in old_res.items():
        res['summary'][k] = v

    res['tables'] = {}
    res['tables']['file_path'] = [
        result_path + '/' + config.need_result_table_file_list[0],
        result_path + '/' + config.need_result_table_file_list[1],
        result_path + '/' + config.need_result_table_file_list[2].format(old_res['resolution'], old_res['resolution']),
        result_path + '/' + config.need_result_table_file_list[3].format(old_res['resolution']),
        result_path + '/' + config.need_result_table_file_list[4].format(old_res['resolution'])
    ]
    res['tables']['table1'] = process_table_file(result_path + '/' + config.need_result_table_file_list[0])
    res['tables']['table2'] = process_table_file(result_path + '/' + config.need_result_table_file_list[1])
    res['tables']['table3'] = process_table_file(result_path + '/' + config.need_result_table_file_list[2].format(old_res['resolution'], old_res['resolution']), head_row_num=10)
    res['tables']['table4'] = process_table_file(result_path + '/' + config.need_result_table_file_list[3].format(old_res['resolution']), head_row_num=10)
    res['tables']['table5'] = process_table_file(result_path + '/' + config.need_result_table_file_list[4].format(old_res['resolution']), head_row_num=10)

    res['figs'] = config.need_result_fig_file_list
    res['figs_name'] = {}
    for k, v in config.need_result_fig_file_list.items():
        res['figs_name'][k] = v.split('/')[-1]
    
    res['check_sec'] = config.check_sec
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

    # TODO cp result file
    for file in data_json['tables']['file_path']:
        os.system('cp {file} {report_path}/result_file'.format(file=file, report_path=report_path))
    for _, file in data_json['figs'].items():
        os.system("cp {result_path}/{file} {report_path}/show_img".format(result_path=result_path, report_path=report_path, file=file))

    # generate report html
    generate_content(main_path + "/Template/split_content_temp.html", data_json, report_path + "/tmp.html")
    for i in range(1, 6):
        fig_html_name = 'Fig' + str(i) + '.html'
        generate_content(main_path + "/Template/full_size_page/" + fig_html_name, data_json, report_path + "/full_size_page/" + fig_html_name)
    merge_html(main_path + "/Template/split_base.html", report_path + "/tmp.html", report_path + "/report.html")
    os.system("rm {report_path}/tmp.html".format(report_path=report_path))




if __name__ == "__main__":
    # resul = "/home/yangguang/work/scRNA_report/result_demo/atac.result"
    main()

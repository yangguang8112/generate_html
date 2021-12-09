

class Config(object):
    def __init__(self) -> None:
        super().__init__()
        self.base_html = ""
        self.need_result_table_file_list = [
            "Result_0_DataStat/Sample_cells_info_stat.xls",
            "Result_1_DataFilter/cellfilter_stat.info",
            "Result_2_Analysis/02_Clustering/final_cluster_stat.xls",
            "Result_2_Analysis/03_Difference/diffCluster_File/All.cluster0.diff_gene.xls",
            "Result_2_Analysis/04_Enrichment/cluster0/GO/cluster_Biological_Process_enrich.list",
            "Result_2_Analysis/04_Enrichment/cluster0/KEGG/cluster_KEGG_pathway_enrich.list",
            "Result_3_Pseudotime/Pseudotime_difference_gene.xls",
            "Result_3_Pseudotime/Pseudotime_info.xls"
        ]
        self.data_json_keys = [
            "cell_stat_table",
            "cell_filter_stat",
            "final_cluster_stat",
            "diffCluster_stat",
            "cluster_Biological_Process_enrich_list",
            "cluster_KEGG_pathway_enrich_list",
            "Pseudotime_difference_gene",
            "Pseudotime_info"
        ]
        self.need_result_fig_file_list = {
            "fig1":[

            ],
            "fig2":[

            ],
            "fig3":[

            ],
            "fig4":[

            ],
            "fig5":[

            ],
            "fig6":[
                
            ]
        }
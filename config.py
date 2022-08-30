

class Config(object):
    def __init__(self) -> None:
        super().__init__()
        self.base_html = ""
        self.need_result_table_file_list =  [
            "Result/Step1/sample_cells_info_stat.xls",
            "Result/Step3/QC/sample.QC.info.txt",
            "Result/Step3/Cluster/res{}/res{}_markerList.txt",
            "Result/Step7/res{}/enrichment/C1/GO/C1_Biological_Process_enrich.list",
            "Result/Step7/res{}/enrichment/C1/KEGG/C1_KEGG_pathway_enrich.list",
        ]
        self.data_json_keys = [
            "cell_stat_table",
            "cell_clonetype",
        ]
        self.check_sec = {
            'cell_filter': 1,
            'sample_merge': 1,
            'cell_cluster_marker': 1,
            'go_kegg': 1,
            'pseudotime': 1,
            'cell_type': 1
        }
        self.need_result_fig_file_list = {
            "fig1": "Result/Figs/Fig1_final.png",
            "fig2": "Result/Figs/Fig2_final.png",
            "fig3": "Result/Figs/Fig3_final.png",
            "fig4": "Result/Figs/Fig4_final.png",
            "fig5": "Result/Figs/Fig5_final.png",
        }

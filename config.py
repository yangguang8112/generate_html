

class Config(object):
    def __init__(self) -> None:
        super().__init__()
        self.base_html = ""
        self.need_result_table_file_list = [
            "Result_0_DataStat/Sample_cells_info_stat.xls",
            "Result_1_DataFilter/cellfilter_stat.info",
            "Result_2_Analysis/02_Clustering/final_cluster_stat.xls",
            "Result_2_Analysis/03_Difference/diffCluster_File/All.cluster0.marker_gene.xls",
            "Result_2_Analysis/04_Enrichment/cluster0/GO/cluster0_Biological_Process_enrich.list",
            "Result_2_Analysis/04_Enrichment/cluster0/KEGG/cluster0_KEGG_pathway_enrich.list",
            "Result_3_Pseudotime/Pseudotime_difference_gene.xls",
            "Result_3_Pseudotime/Pseudotime_info.xls",
            "Result_2_Analysis/05_CellAnnotation/final.cell_annotation_statInfo.xls"
        ]
        self.data_json_keys = [
            "cell_stat_table",
            "cell_filter_stat",
            "final_cluster_stat",
            "diffCluster_stat",
            "cluster0_Biological_Process_enrich_list",
            "cluster0_KEGG_pathway_enrich_list",
            "Pseudotime_difference_gene",
            "Pseudotime_info",
            "cell_annotation_statinfo"
        ]
        self.check_keys = ['cell_filter', 'sample_merge', 'cell_cluster_marker', 'go_kegg', 'pseudotime', 'cell_type']
        self.check_sec = {
            'cell_filter': 1,
            'sample_merge': 1,
            'cell_cluster_marker': 1,
            'go_kegg': 1,
            'pseudotime': 1,
            'cell_type': 1
        }
        # self.need_result_fig_file_list = {
        #     "fig1":[
        #         "Result_1_DataFilter/All_sample_nofilter.vln.png",
        #         "Result_1_DataFilter/All_sample_filter.vln.png",
        #         "Result_1_DataFilter/All_sample_nofilter.scatter.png",
        #         "Result_1_DataFilter/All_sample_filter.scatter.png",
        #         "Result_1_DataFilter/All.libarary.transcriptome.similarity.png"
        #     ],
        #     "fig2":[
        #         "Result_2_Analysis/02_Clustering/final_cluster_umap_batch.png",
        #         "Result_2_Analysis/02_Clustering/final_cluster_umap_sample.png",
        #         "Result_2_Analysis/02_Clustering/final_cluster_umap_splitBatch.png",
        #         "Result_2_Analysis/02_Clustering/final_cluster_umap_splitSample.png"
        #     ],
        #     "fig3":[
        #         "Result_2_Analysis/02_Clustering/final_cluster_umap.png",
        #         "Result_2_Analysis/03_Difference/diffCluster_picture/All.cluster0_top_uniqstr__markerUmap.png",
        #         "Result_2_Analysis/03_Difference/diffCluster_picture/dotplot_and_barplot.png",
        #         "Result_2_Analysis/03_Difference/diffCluster_picture/All.cluster0_top_uniqstr__markerVln.png"
        #     ],
        #     "fig4":[
        #         "Result_2_Analysis/03_Difference/diffCluster_volcano/All.cluster0.volcano.png",
        #         "Result_2_Analysis/03_Difference/diffCluster_picture/top_markergene_heatmap.png",
        #         "Result_2_Analysis/04_Enrichment/BP_dotplot.png",
        #         "Result_2_Analysis/04_Enrichment/KEGG_dotplot.png"
        #     ],
        #     "fig5":[
        #         "Result_3_Pseudotime/cell_trajectory_cluster_split.png",
        #         "Result_3_Pseudotime/cell_trajectory_Pseudotime.png",
        #         "Result_3_Pseudotime/cell_trajectory_heatmap.png",
        #         "Result_3_Pseudotime/cell_trajectory_topGene_marker_cluster.png"
        #     ],
        #     "fig6":[
        #         "Result_2_Analysis/05_CellAnnotation/final.cluster_annotation_umap.png",
        #         "Result_2_Analysis/05_CellAnnotation/final.cluster_annotation_sample_barplot.png"
        #     ]
        # }
        self.final_figs = {
            "fig1": "../Backup/07_show_img/fig1_final.png",
            "fig2": "../Backup/07_show_img/fig2_final.png",
            "fig3": "../Backup/07_show_img/fig3_final.png",
            "fig4": "../Backup/07_show_img/fig4_final.png",
            "fig5": "../Backup/07_show_img/fig5_final.png",
            "fig6": "../Backup/07_show_img/fig6_final.png"
        }

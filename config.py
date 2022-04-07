

class Config(object):
    def __init__(self) -> None:
        super().__init__()
        self.base_html = ""
        self.need_result_table_file_list = {
            'TCR': [
                "Result_01_report/TCR_library_cells_info_stat.xls",
                "Result_03_sample/TCR/00.Clonetype/TCR_clonetype.tsv"

            ],
            'BCR': [
                "Result_01_report/BCR_library_cells_info_stat.xls",
                "Result_03_sample/BCR/00.Clonetype/BCR_clonetype.tsv"
            ]
        }
        
        # [
        #     "Result_0_DataStat/Sample_cells_info_stat.xls",
        #     "Result_1_DataFilter/cellfilter_stat.info",
        #     "Result_2_Analysis/02_Clustering/final_cluster_stat.xls",
        #     "Result_2_Analysis/03_Difference/diffCluster_File/All.cluster0.marker_gene.xls",
        #     "Result_2_Analysis/04_Enrichment/cluster0/GO/cluster0_Biological_Process_enrich.list",
        #     "Result_2_Analysis/04_Enrichment/cluster0/KEGG/cluster0_KEGG_pathway_enrich.list",
        #     "Result_3_Pseudotime/Pseudotime_difference_gene.xls",
        #     "Result_3_Pseudotime/Pseudotime_info.xls"
        # ]
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
        # self.need_result_fig_file_list = {
        #     "fig1": {
        #         "TCR": [
        #             "Result_03_sample/TCR/01.exploratory/01_Exploratory_1.png",
        #             "Result_03_sample/TCR/01.exploratory/01_Exploratory_3.png",
        #             "Result_03_sample/TCR/02.Clonality/02_Clonality_2.png",
        #             "Result_03_sample/TCR/02.Clonality/02_Clonality_4.png"
        #         ],
        #         "BCR": [
        #             "Result_03_sample/BCR/01.exploratory/01_Exploratory_1.png",
        #             "Result_03_sample/BCR/01.exploratory/01_Exploratory_3.png",
        #             "Result_03_sample/BCR/02.Clonality/02_Clonality_2.png",
        #             "Result_03_sample/BCR/02.Clonality/02_Clonality_4.png"
        #         ]
        #     },
        #     "fig2": {
        #         "TCR": [
        #             "Result_03_sample/TCR/03.Overlap/03_overlap_public1.png",
        #             "Result_03_sample/TCR/03.Overlap/03_overlap_morisita.png"
        #         ],
        #         "BCR": [
        #             "Result_03_sample/BCR/03.Overlap/03_overlap_public1.png",
        #             "Result_03_sample/BCR/03.Overlap/03_overlap_morisita.png"
        #         ]
        #     },
        #     "fig3": {
        #         "TCR": [
        #             "Result_03_sample/TCR/04.Diversity/04_diversity_chao1.png",
        #             "Result_03_sample/TCR/04.Diversity/04_diversity_d50.png",
        #             "Result_03_sample/TCR/04.Diversity/04_diversity_gini.png",
        #             "Result_03_sample/TCR/04.Diversity/04_diversity_raref.png"
        #         ],
        #         "BCR": [
        #             "Result_03_sample/BCR/04.Diversity/04_diversity_chao1.png",
        #             "Result_03_sample/BCR/04.Diversity/04_diversity_d50.png",
        #             "Result_03_sample/BCR/04.Diversity/04_diversity_gini.png",
        #             "Result_03_sample/BCR/04.Diversity/04_diversity_raref.png"
        #         ]
        #     },
        #     "fig4": {
        #         "TCR": [
        #             "Result_03_sample/TCR/05.Geneusage/hs.trav.barplot/P11S4.png",
        #             "Result_03_sample/TCR/05.Geneusage/hs.trbv.polarplot/P11S4.png",
        #             "Result_03_sample/TCR/05.Geneusage/circosPlot/P11S4.png",
        #             "Result_03_sample/TCR/05.Geneusage/all/TRBV_js.png"
        #         ],
        #         "BCR": [
        #             "Result_03_sample/BCR/05.Geneusage/hs.ighv.barplot/P11S4.png",
        #             "Result_03_sample/BCR/05.Geneusage/hs.igkv.polarplot/P11S4.png",
        #             "Result_03_sample/BCR/05.Geneusage/circosPlot/P11S4.png",
        #             "Result_03_sample/BCR/05.Geneusage/all/IGHV_js.png"
        #         ]
        #     },
        #     "fig5": {
        #         "TCR": [
        #             "Result_03_sample/TCR/06.Tracking/track_top10_of_aa_from_P11S4.png",
        #             "Result_03_sample/TCR/06.Tracking/track_top10_of_aa_from_P18S1.png"
        #         ],
        #         "BCR": [
        #             "Result_03_sample/BCR/06.Tracking/track_top10_of_aa_from_P11S4.png",
        #             "Result_03_sample/BCR/06.Tracking/track_top10_of_aa_from_P18S1.png"
        #         ]
        #     },
        #     "fig6": {
        #         "TCR": [
        #             "Result_03_sample/TCR/07.Kmer/01_top10_kmer.png",
        #             "Result_03_sample/TCR/07.Kmer/01_motifs2.png"
        #         ],
        #         "BCR": [
        #             "Result_03_sample/BCR/07.Kmer/01_top10_kmer.png",
        #             "Result_03_sample/BCR/07.Kmer/01_motifs2.png"
        #         ]
        #     },
        #     "fig7": {
        #         "TCR": [
        #             "Result_04_cluster/TCR/08.UMAP/UMAP1_cloneType.png",
        #             "Result_04_cluster/TCR/08.UMAP/UMAP2_rare_abundance.png"
        #         ],
        #         "BCR": [
        #             "Result_04_cluster/BCR/08.UMAP/UMAP1_cloneType.png",
        #             "Result_04_cluster/BCR/08.UMAP/UMAP2_rare_abundance.png"
        #         ]
        #     }
        # }
        self.final_figs = {
            "fig1": {
                "TCR": "Backup/picMerge/TCR_fig1_final.png",
                "BCR": "Backup/picMerge/BCR_fig1_final.png"
            },
            "fig2": {
                "TCR": "Backup/picMerge/TCR_fig2_final.png",
                "BCR": "Backup/picMerge/BCR_fig2_final.png"
            },
            "fig3": {
                "TCR": "Backup/picMerge/TCR_fig3_final.png",
                "BCR": "Backup/picMerge/BCR_fig3_final.png"
            },
            "fig4": {
                "TCR": "Backup/picMerge/TCR_fig4_final.png",
                "BCR": "Backup/picMerge/BCR_fig4_final.png"
            },
            "fig5": {
                "TCR":"Backup/picMerge/TCR_fig5_final.png",
                "BCR": "Backup/picMerge/BCR_fig5_final.png"
            },
            "fig6": {
                "TCR": "Backup/picMerge/TCR_fig6_final.png",
                "BCR": "Backup/picMerge/BCR_fig6_final.png"
            },
            "fig7": {
                "TCR": "Backup/picMerge/TCR_fig7_final.png",
                "BCR": "Backup/picMerge/BCR_fig7_final.png"
            }
        }

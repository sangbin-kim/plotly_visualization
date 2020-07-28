import data_processing
import visualization


line_6_1 = 'E66C CNA6-1'
filename_6_1 = r"C:\\Users\\lg\\Desktop\\정지후가동\\CNA6\\6-1\\"
csv_filename_6_1 = r'D:\#.Secure Work Folder\정지후가동\CNA6\lami vision data\6-1.csv'

line_6_2= 'E66C CNA6-2'
filename_6_2 = r"C:\\Users\\lg\\Desktop\\정지후가동\\CNA6\\6-2\\"
csv_filename_6_2 = r'D:\#.Secure Work Folder\정지후가동\CNA6\lami vision data\6-2.csv'

line_6_3 = 'E66C CNA6-3'
filename_6_3 = r"C:\\Users\\lg\\Desktop\\정지후가동\\CNA6\\6-3\\"
csv_filename_6_3 = r'D:\#.Secure Work Folder\정지후가동\CNA6\lami vision data\6-3.csv'

line_6_4 = 'E66C CNA6-4'
filename_6_4 = r"C:\\Users\\lg\\Desktop\\정지후가동\\CNA6\\6-4\\"
csv_filename_6_4 = r'D:\#.Secure Work Folder\정지후가동\CNA6\lami vision data\6-4.csv'


lines = [line_6_1, line_6_2, line_6_3, line_6_4]
filenames = [filename_6_1, filename_6_2, filename_6_3, filename_6_4]
csv_filenames = [csv_filename_6_1, csv_filename_6_2, csv_filename_6_3, csv_filename_6_4]

for line, filename, csv_filename in zip(lines, filenames, csv_filenames):

    Line_6_1 = CNA6_data_processing.LineStopProcessing(csv_filename, 500, 30)

    Line_6_1.timecolumn()
    Line_6_1.counting()

    Line_6_1.summaryby_interval(x_axis= 250,
                         start= 30,
                         end= 600,
                         C_R12L12_LSL= 1.75,
                         TPC_LSL= 18.15,
                         G_R12L12_LSL= 0.45,
                         TPA_LSL= 0.0,
                         C_TL_LSL= 2.5,
                         C_BL_LSL= 3.2,
                         G_TL_LSL= 0.4,
                         G_BL_LSL= 1.1,
                         TWA_LSL= 44.0,
                         TWC_LSL= 44.0,
                         M_TL_LSL= 0.5,
                         M_TL_USL= 4.3,
                         C_R12L12_USL= 4.00,
                         TPC_USL= 19.95,
                         G_R12L12_USL= 2.05,
                         TPA_USL= 0.0,
                         C_TL_USL= 4.3,
                         C_BL_USL= 5.0,
                         G_TL_USL= 1.6,
                         G_BL_USL= 2.3,
                         TWA_USL= 46.0,
                         TWC_USL= 46.0)

    Line_6_1.summaryby_total(x_axis= 250,
                             C_R12L12_LSL=1.75,
                             TPC_LSL=18.15,
                             G_R12L12_LSL=0.45,
                             TPA_LSL=0.0,
                             C_TL_LSL=2.5,
                             C_BL_LSL=3.2,
                             G_TL_LSL=0.4,
                             G_BL_LSL=1.1,
                             TWA_LSL=44.0,
                             TWC_LSL=44.0,
                             M_TL_LSL=0.5,
                             M_TL_USL=4.3,
                             C_R12L12_USL=4.00,
                             TPC_USL=19.95,
                             G_R12L12_USL=2.05,
                             TPA_USL=0.0,
                             C_TL_USL=4.3,
                             C_BL_USL=5.0,
                             G_TL_USL=1.6,
                             G_BL_USL=2.3,
                             TWA_USL=46.0,
                             TWC_USL=46.0)
    Line_6_1.utility()

    plot_6_1 = CNA6_graph.plot(x_axis = 250,
                                        interval_data = Line_6_1.sum_data_int,
                                        sum_data_interval = Line_6_1.summaryby_time,
                                        sum_data_total = Line_6_1.summaryby_total,
                                        sum_utility_int = Line_6_1.utility_interval,
                                        sum_utility_total = Line_6_1.utility_total ,
                                        filename = filename,
                                        line = line,
                     C_R12L12_Target = 2.75,
                     TPC_Target = 19.05,
                     G_R12L12_Target = 1.25,
                     TPA_Target = 0.0,
                     C_TL_Target = 3.4,
                     C_BL_Target = 4.1,
                     G_TL_Target = 1.0,
                     G_BL_Target = 1.7,
                     TWA_Target = 45.0,
                     TWC_Target = 45.0,
                     M_TL_Target = 2.4,
                     M_BL_Target = 2.4)

    plot_6_1.x_graph()
    plot_6_1.y_tab_graph()
    plot_6_1.sm_graph()
    plot_6_1.summary_total()

    Line_6_1.usedata.to_csv(filename + 'Counted_rawdata.csv')
    Line_6_1.summaryby_time.to_csv(filename + 'summaryby_time.csv')
    Line_6_1.summaryby_total.to_csv(filename + 'summaryby_total.csv')
    Line_6_1.utility_total.to_csv(filename + 'utility_total.csv')
    Line_6_1.utility_interval.to_csv(filename + 'utility_interval.csv')

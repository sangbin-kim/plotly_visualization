import pandas as pd


class LineStopProcessing:
    def __init__(self, rawdata, countcell, delaytime):
        self.rawdata = pd.read_csv(rawdata, header=0, engine='python')
        self.usedata = self.rawdata
        self.countcell = countcell
        self.delaytime = delaytime
        self.time = pd.DataFrame()

    def timecolumn(self):
        self.time['Time'] = self.usedata["Time"]
        self.time['Time'] = self.time['Time'].apply(lambda x: '{0:0>6}'.format(x))

        self.time['Hour'] = self.time['Time'].str[0:2]
        self.time['Min'] = self.time['Time'].str[2:4]
        self.time['Sec'] = self.time['Time'].str[4:6]

        self.usedata['Hour'] = self.time["Hour"].astype(int)
        self.usedata['Minute'] = self.time["Min"].astype(int)
        self.usedata['Second'] = self.time["Sec"].astype(int)
        self.usedata['Total Sec'] = self.usedata["Hour"] * 3600 + self.usedata["Minute"] * 60 + self.usedata["Second"]
        self.usedata['diff Sec'] = self.usedata['Total Sec'].diff()
        self.usedata['Group'] = 0
        self.usedata['diff_Sec1'] = 0
        self.usedata['Cell No'] = 0
        self.stop = self.usedata.loc[self.usedata['diff Sec'] > int(self.delaytime)]
        self.stop.index.name = 'Cell No1'
        self.stop.reset_index(inplace=True)
        self.countrow = len(self.usedata.index)
        self.grouped_500 = []

    def counting(self):
        # Labeling Group number & Total Line stop sec
        for i in range(len(self.stop.index)):
            cell_cnting = self.stop.loc[i, 'Cell No1']
            diff_sec = self.stop.loc[i, 'diff Sec']

            self.usedata.loc[cell_cnting:self.countrow, 'Group'] = i + 1
            self.usedata.loc[cell_cnting:self.countrow, 'diff_Sec1'] = diff_sec

        # Labeling cell number from each line stop
        c = 0
        while c < (len(self.stop.index)):

            stop_cell_no = self.stop.loc[c, 'Cell No1']
            d = 0
            while d < int(self.countcell):
                self.usedata.loc[(stop_cell_no + d):(stop_cell_no + d), 'Cell No'] = d + 1
                d = d + 1
            c = c + 1

        gr = 1
        while gr < (len(self.stop.index)):

            grouped_500 = self.usedata[self.usedata['Group'] == gr]

            if len(grouped_500) >= self.countcell:
                self.grouped_500.append(grouped_500)

            gr = gr + 1

        self.grouped_500 = pd.concat(self.grouped_500)

    def summaryby_interval(self, start, end, x_axis,
                           C_R12L12_LSL,
                           TPC_LSL,
                           G_R12L12_LSL,
                           TPA_LSL,
                           C_TL_LSL,
                           C_BL_LSL,
                           G_TL_LSL,
                           G_BL_LSL,
                           TWA_LSL,
                           TWC_LSL,
                           M_TL_LSL,
                           M_TL_USL,
                           C_R12L12_USL,
                           TPC_USL,
                           G_R12L12_USL,
                           TPA_USL,
                           C_TL_USL,
                           C_BL_USL,
                           G_TL_USL,
                           G_BL_USL,
                           TWA_USL,
                           TWC_USL):

        self.sum_data_int = self.usedata[
            (self.usedata['diff_Sec1'] >= int(start)) & (self.usedata['diff_Sec1'] < int(end))]
        self.summaryby_time = pd.DataFrame(
            columns=['Cell No', 'Total Count', 'NG Total Count', 'NG Rate (%)', 'X Total', 'X NG Rate (%)', 'Y Total',
                     'Y NG Rate (%)', 'Tab Total', 'Tab NG Rate (%)', 'SM Total', 'SM NG Rate (%)'])
        self.count = len(self.usedata.index)

        C_R12L12_LSL = float(C_R12L12_LSL)
        TPC_LSL = float(TPC_LSL)
        G_R12L12_LSL = float(G_R12L12_LSL)
        TPA_LSL = float(TPA_LSL)

        C_TL_LSL = float(C_TL_LSL)
        C_BL_LSL = float(C_BL_LSL)
        G_TL_LSL = float(G_TL_LSL)
        G_BL_LSL = float(G_BL_LSL)

        TWA_LSL = float(TWA_LSL)
        TWC_LSL = float(TWC_LSL)
        M_TL_LSL = float(M_TL_LSL)
        M_TL_USL = float(M_TL_USL)

        C_R12L12_USL = float(C_R12L12_USL)
        TPC_USL = float(TPC_USL)
        G_R12L12_USL = float(G_R12L12_USL)
        TPA_USL = float(TPA_USL)

        C_TL_USL = float(C_TL_USL)
        C_BL_USL = float(C_BL_USL)
        G_TL_USL = float(G_TL_USL)
        G_BL_USL = float(G_BL_USL)

        TWA_USL = float(TWA_USL)
        TWC_USL = float(TWC_USL)

        f = 0
        while f < int(x_axis):
            f = f + 1
            total_count = len(self.sum_data_int[self.sum_data_int['Cell No'] == f].index)
            ng_count_by_cell = len(
                self.sum_data_int[(self.sum_data_int['Cell No'] == f) & (self.sum_data_int['Result'] != 'OK')].index)
            ng_rate_by_cell = (len(
                self.sum_data_int[(self.sum_data_int['Cell No'] == f) & (
                            self.sum_data_int['Result'] != 'OK')].index) / self.count) * 100
            x_total_count = len(
                self.sum_data_int[(self.sum_data_int['Cell No'] == f) & (self.sum_data_int['Result'] != 'OK') & (
                        ((self.sum_data_int['C_L1'] < C_R12L12_LSL) | (self.sum_data_int['C_L1'] > C_R12L12_USL)) |
                        ((self.sum_data_int['C_L2'] < C_R12L12_LSL) | (self.sum_data_int['C_L2'] > C_R12L12_USL)) |
                        ((self.sum_data_int['C_R1'] < C_R12L12_LSL) | (self.sum_data_int['C_R1'] > C_R12L12_USL)) |
                        ((self.sum_data_int['C_R2'] < C_R12L12_LSL) | (self.sum_data_int['C_R2'] > C_R12L12_USL)) |
                        ((self.sum_data_int['G_L1'] < G_R12L12_LSL) | (self.sum_data_int['G_L1'] > G_R12L12_USL)) |
                        ((self.sum_data_int['G_L2'] < G_R12L12_LSL) | (self.sum_data_int['G_L2'] > G_R12L12_USL)) |
                        ((self.sum_data_int['G_R1'] < G_R12L12_LSL) | (self.sum_data_int['G_R1'] > G_R12L12_USL)) |
                        ((self.sum_data_int['G_R2'] < G_R12L12_LSL) | (self.sum_data_int['G_R2'] > G_R12L12_USL)) |
                        ((self.sum_data_int['TPC'] < TPC_LSL) | (self.sum_data_int['TPC'] > TPC_USL)))].index)
            x_ng_rate_by_cell = (x_total_count / self.count) * 100
            y_total_count = len(
                self.sum_data_int[(self.sum_data_int['Cell No'] == f) & (self.sum_data_int['Result'] != 'OK') & (
                        ((self.sum_data_int['C_T'] < C_TL_LSL) | (self.sum_data_int['C_T'] > C_TL_USL)) |
                        ((self.sum_data_int['C_B'] < C_BL_LSL) | (self.sum_data_int['C_B'] > C_BL_USL)) |
                        ((self.sum_data_int['G_T1'] < G_TL_LSL) | (self.sum_data_int['G_T1'] > G_TL_USL)) |
                        ((self.sum_data_int['G_B1'] < G_BL_LSL) | (self.sum_data_int['G_B1'] > G_BL_USL)) |
                        ((self.sum_data_int['G_T2'] < G_TL_LSL) | (self.sum_data_int['G_T2'] > G_TL_USL)) |
                        ((self.sum_data_int['G_B2'] < G_BL_LSL) | (self.sum_data_int['G_B2'] > G_BL_USL))
                )].index)

            y_ng_rate_by_cell = (y_total_count / self.count) * 100
            tab_total_count = len(
                self.sum_data_int[(self.sum_data_int['Cell No'] == f) & (self.sum_data_int['Result'] != 'OK') & (
                        ((self.sum_data_int['TWA'] < TWA_LSL) | (self.sum_data_int['TWA'] > TWA_USL)) |
                        ((self.sum_data_int['TWC'] < TWC_LSL) | (self.sum_data_int['TWC'] > TWC_USL))
                )].index)
            tab_ng_rate_by_cell = (tab_total_count / self.count) * 100
            mis_match_total_count = len(
                self.sum_data_int[(self.sum_data_int['Cell No'] == f) & (self.sum_data_int['Result'] != 'OK') & (
                        ((self.sum_data_int['M_BR'] < M_TL_LSL) | (self.sum_data_int['M_BR'] > M_TL_USL)) |
                        ((self.sum_data_int['M_TR'] < M_TL_LSL) | (self.sum_data_int['M_TR'] > M_TL_USL)) |
                        ((self.sum_data_int['M_BL'] < M_TL_LSL) | (self.sum_data_int['M_BL'] > M_TL_USL)) |
                        ((self.sum_data_int['M_TL'] < M_TL_LSL) | (self.sum_data_int['M_TL'] > M_TL_USL))
                )].index)
            mis_match_ng_rate_by_cell = (mis_match_total_count / self.count) * 100

            self.summaryby_time.loc[f] = [f,
                                          total_count,
                                          ng_count_by_cell,
                                          ng_rate_by_cell,
                                          x_total_count,
                                          x_ng_rate_by_cell,
                                          y_total_count,
                                          y_ng_rate_by_cell,
                                          tab_total_count,
                                          tab_ng_rate_by_cell,
                                          mis_match_total_count,
                                          mis_match_ng_rate_by_cell]

    def summaryby_total(self, x_axis,
                        C_R12L12_LSL,
                        TPC_LSL,
                        G_R12L12_LSL,
                        TPA_LSL,
                        C_TL_LSL,
                        C_BL_LSL,
                        G_TL_LSL,
                        G_BL_LSL,
                        TWA_LSL,
                        TWC_LSL,
                        M_TL_LSL,
                        M_TL_USL,
                        C_R12L12_USL,
                        TPC_USL,
                        G_R12L12_USL,
                        TPA_USL,
                        C_TL_USL,
                        C_BL_USL,
                        G_TL_USL,
                        G_BL_USL,
                        TWA_USL,
                        TWC_USL):

        self.sum_data_total = self.usedata
        self.summaryby_total = pd.DataFrame(
            columns=['Cell No', 'Total Count', 'NG Total Count', 'NG Rate (%)', 'X Total', 'X NG Rate (%)', 'Y Total',
                     'Y NG Rate (%)', 'Tab Total', 'Tab NG Rate (%)', 'SM Total', 'SM NG Rate (%)'])
        self.count = len(self.usedata.index)

        C_R12L12_LSL = float(C_R12L12_LSL)
        TPC_LSL = float(TPC_LSL)
        G_R12L12_LSL = float(G_R12L12_LSL)
        TPA_LSL = float(TPA_LSL)

        C_TL_LSL = float(C_TL_LSL)
        C_BL_LSL = float(C_BL_LSL)
        G_TL_LSL = float(G_TL_LSL)
        G_BL_LSL = float(G_BL_LSL)

        TWA_LSL = float(TWA_LSL)
        TWC_LSL = float(TWC_LSL)
        M_TL_LSL = float(M_TL_LSL)
        M_TL_USL = float(M_TL_USL)

        C_R12L12_USL = float(C_R12L12_USL)
        TPC_USL = float(TPC_USL)
        G_R12L12_USL = float(G_R12L12_USL)
        TPA_USL = float(TPA_USL)

        C_TL_USL = float(C_TL_USL)
        C_BL_USL = float(C_BL_USL)
        G_TL_USL = float(G_TL_USL)
        G_BL_USL = float(G_BL_USL)

        TWA_USL = float(TWA_USL)
        TWC_USL = float(TWC_USL)

        f = 0

        while f < int(x_axis):
            f = f + 1
            total_count = len(self.sum_data_total[self.sum_data_total['Cell No'] == f].index)
            ng_count_by_cell = len(self.sum_data_total[(self.sum_data_total['Cell No'] == f) & (
                        self.sum_data_total['Result'] != 'OK')].index)
            ng_rate_by_cell = (len(
                self.sum_data_total[(self.sum_data_total['Cell No'] == f) & (
                            self.sum_data_total['Result'] != 'OK')].index) / self.count) * 100
            x_total_count = len(
                self.sum_data_total[(self.sum_data_total['Cell No'] == f) & (self.sum_data_total['Result'] != 'OK') & (
                        ((self.sum_data_total['C_L1'] < C_R12L12_LSL) | (self.sum_data_total['C_L1'] > C_R12L12_USL)) |
                        ((self.sum_data_total['C_L2'] < C_R12L12_LSL) | (self.sum_data_total['C_L2'] > C_R12L12_USL)) |
                        ((self.sum_data_total['C_R1'] < C_R12L12_LSL) | (self.sum_data_total['C_R1'] > C_R12L12_USL)) |
                        ((self.sum_data_total['C_R2'] < C_R12L12_LSL) | (self.sum_data_total['C_R2'] > C_R12L12_USL)) |
                        ((self.sum_data_total['G_L1'] < G_R12L12_LSL) | (self.sum_data_total['G_L1'] > G_R12L12_USL)) |
                        ((self.sum_data_total['G_L2'] < G_R12L12_LSL) | (self.sum_data_total['G_L2'] > G_R12L12_USL)) |
                        ((self.sum_data_total['G_R1'] < G_R12L12_LSL) | (self.sum_data_total['G_R1'] > G_R12L12_USL)) |
                        ((self.sum_data_total['G_R2'] < G_R12L12_LSL) | (self.sum_data_total['G_R2'] > G_R12L12_USL)) |
                        ((self.sum_data_total['TPC'] < TPC_LSL) | (self.sum_data_total['TPC'] > TPC_USL)))].index)
            x_ng_rate_by_cell = (x_total_count / self.count) * 100
            y_total_count = len(
                self.sum_data_int[(self.sum_data_int['Cell No'] == f) & (self.sum_data_int['Result'] != 'OK') & (
                        ((self.sum_data_total['C_T'] < C_TL_LSL) | (self.sum_data_total['C_T'] > C_TL_USL)) |
                        ((self.sum_data_total['C_B'] < C_BL_LSL) | (self.sum_data_total['C_B'] > C_BL_USL)) |
                        ((self.sum_data_total['G_T1'] < G_TL_LSL) | (self.sum_data_total['G_T1'] > G_TL_USL)) |
                        ((self.sum_data_total['G_B1'] < G_BL_LSL) | (self.sum_data_total['G_B1'] > G_BL_USL)) |
                        ((self.sum_data_total['G_T2'] < G_BL_LSL) | (self.sum_data_total['G_T2'] > G_BL_USL)) |
                        ((self.sum_data_total['G_B2'] < G_BL_LSL) | (self.sum_data_total['G_B2'] > G_BL_USL))
                )].index)

            y_ng_rate_by_cell = (y_total_count / self.count) * 100
            tab_total_count = len(
                self.sum_data_total[(self.sum_data_total['Cell No'] == f) & (self.sum_data_total['Result'] != 'OK') & (
                        ((self.sum_data_total['TWA'] < TWA_LSL) | (self.sum_data_total['TWA'] > TWA_USL)) |
                        ((self.sum_data_total['TWC'] < TWC_LSL) | (self.sum_data_total['TWC'] > TWC_USL))
                )].index)
            tab_ng_rate_by_cell = (tab_total_count / self.count) * 100
            mis_match_total_count = len(
                self.sum_data_total[(self.sum_data_total['Cell No'] == f) & (self.sum_data_total['Result'] != 'OK') & (
                        ((self.sum_data_total['M_BR'] < M_TL_LSL) | (self.sum_data_total['M_BR'] > M_TL_USL)) |
                        ((self.sum_data_total['M_TR'] < M_TL_LSL) | (self.sum_data_total['M_TR'] > M_TL_USL)) |
                        ((self.sum_data_total['M_BL'] < M_TL_LSL) | (self.sum_data_total['M_BL'] > M_TL_USL)) |
                        ((self.sum_data_total['M_TL'] < M_TL_LSL) | (self.sum_data_total['M_TL'] > M_TL_USL))

                )].index)
            mis_match_ng_rate_by_cell = (mis_match_total_count / self.count) * 100

            self.summaryby_total.loc[f] = [f,
                                           total_count,
                                           ng_count_by_cell,
                                           ng_rate_by_cell,
                                           x_total_count,
                                           x_ng_rate_by_cell,
                                           y_total_count,
                                           y_ng_rate_by_cell,
                                           tab_total_count,
                                           tab_ng_rate_by_cell,
                                           mis_match_total_count,
                                           mis_match_ng_rate_by_cell]

    def utility(self):

        count = len(self.usedata)
        utility_dataset = [self.sum_data_total, self.sum_data_int]
        result = []

        for utility in utility_dataset:
            # NG count by location ----------------------------------------------------------------------------------------

            vision = len(
                utility[(utility['Result'] != 'OK') & (
                        (utility['Cell No'] >= 1) & (utility['Cell No'] <= 2))])
            vision_shortcv = len(
                utility[(utility['Result'] != 'OK') & (
                        (utility['Cell No'] >= 3) & (utility['Cell No'] <= 13))])
            finalcutter = len(
                utility[(utility['Result'] != 'OK') & (
                        (utility['Cell No'] >= 13) & (utility['Cell No'] <= 17))])
            finalcutter_finalcv = len(
                utility[(utility['Result'] != 'OK') & (
                        (utility['Cell No'] >= 16) & (utility['Cell No'] <= 25))])
            finalcv_lamiroll = len(
                utility[(utility['Result'] != 'OK') & (
                        (utility['Cell No'] >= 26) & (utility['Cell No'] <= 40))])
            lamiroll = len(
                utility[(utility['Result'] != 'OK') &
                        (utility['Cell No'] == 41)])
            lamiroll_heaterep = len(
                utility[(utility['Result'] != 'OK') & (
                        (utility['Cell No'] >= 42) & (utility['Cell No'] <= 45))])
            heaterep_heatersp = len(
                utility[(utility['Result'] != 'OK') & (
                        (utility['Cell No'] >= 46) & (utility['Cell No'] <= 61))])
            heatersp_niproll = len(
                utility[(utility['Result'] != 'OK') & (
                        (utility['Cell No'] >= 62) & (utility['Cell No'] <= 67))])
            uppercutter = len(
                utility[(utility['Result'] != 'OK') & (
                        (utility['Cell No'] >= 63) & (utility['Cell No'] <= 73))])
            centercutter = len(
                utility[(utility['Result'] != 'OK') & (
                        (utility['Cell No'] >= 70) & (utility['Cell No'] <= 80))])
            upepc = len(
                utility[(utility['Result'] != 'OK') & (
                        (utility['Cell No'] >= 79) & (utility['Cell No'] <= 89))])
            centerepc = len(
                utility[(utility['Result'] != 'OK') & (
                        (utility['Cell No'] >= 90) & (utility['Cell No'] <= 100))])
            centeras = len(
                utility[(utility['Result'] != 'OK') & (
                        (utility['Cell No'] >= 171) & (utility['Cell No'] <= 181))])
            upas = len(
                utility[(utility['Result'] != 'OK') & (
                        (utility['Cell No'] >= 176) & (utility['Cell No'] <= 186))])

            # Cell count by location ----------------------------------------------------------------------------------------

            vision_t = len(
                utility[
                    (utility['Cell No'] >= 1) & (utility['Cell No'] <= 2)])
            vision_shortcv_t = len(
                utility[
                    (utility['Cell No'] >= 3) & (utility['Cell No'] <= 13)])
            finalcutter_t = len(
                utility[
                    (utility['Cell No'] >= 13) & (utility['Cell No'] <= 17)])
            finalcutter_finalcv_t = len(
                utility[
                    (utility['Cell No'] >= 16) & (utility['Cell No'] <= 25)])
            finalcv_lamiroll_t = len(
                utility[
                    (utility['Cell No'] >= 26) & (utility['Cell No'] <= 40)])
            lamiroll_t = len(
                utility[
                    (utility['Cell No'] == 41)])
            lamiroll_heaterep_t = len(
                utility[
                    (utility['Cell No'] >= 42) & (utility['Cell No'] <= 45)])
            heaterep_heatersp_t = len(
                utility[
                    (utility['Cell No'] >= 46) & (utility['Cell No'] <= 61)])
            heatersp_niproll_t = len(
                utility[
                    (utility['Cell No'] >= 62) & (utility['Cell No'] <= 67)])
            uppercutter_t = len(
                utility[
                    (utility['Cell No'] >= 63) & (utility['Cell No'] <= 73)])
            centercutter_t = len(
                utility[
                    (utility['Cell No'] >= 70) & (utility['Cell No'] <= 80)])
            upepc_t = len(
                utility[
                    (utility['Cell No'] >= 79) & (utility['Cell No'] <= 89)])
            centerepc_t = len(
                utility[
                    (utility['Cell No'] >= 90) & (utility['Cell No'] <= 100)])
            centeras_t = len(
                utility[
                    (utility['Cell No'] >= 171) & (utility['Cell No'] <= 181)])
            upas_t = len(
                utility[
                    (utility['Cell No'] >= 176) & (utility['Cell No'] <= 186)])

            utility_data = pd.DataFrame(
                columns=['Section', 'Total (EA)', 'Section Total (EA)', 'NG Count (EA)', 'NG Rate from the Section (%)',
                         'NG Rate from Total (%)'])

            utility_data.loc[0] = ['vision', count, vision_t, vision, ((vision / vision_t) * 100),
                                   ((vision / count) * 100)]
            utility_data.loc[1] = ['Vision ~ Short C/V', count, vision_shortcv_t, vision_shortcv,
                                   ((vision_shortcv / vision_shortcv_t) * 100),
                                   ((vision_shortcv / count) * 100)]
            utility_data.loc[2] = ['F/C', count, finalcutter_t, finalcutter, ((finalcutter / finalcutter_t) * 100),
                                   ((finalcutter / count) * 100)]
            utility_data.loc[3] = ['F/C ~ Final C/V', count, finalcutter_finalcv_t, finalcutter_finalcv,
                                   ((finalcutter_finalcv / finalcutter_finalcv_t) * 100),
                                   ((finalcutter_finalcv / count) * 100)]
            utility_data.loc[4] = ['Final C/V ~ Lami Roll', count, finalcv_lamiroll_t, finalcv_lamiroll,
                                   ((finalcv_lamiroll / finalcv_lamiroll_t) * 100),
                                   ((finalcv_lamiroll / count) * 100)]
            utility_data.loc[5] = ['Lami Roll', count, lamiroll_t, lamiroll, ((lamiroll / lamiroll_t) * 100),
                                   ((lamiroll / count) * 100)]
            utility_data.loc[6] = ['Lami Roll ~ HZ EP', count, lamiroll_heaterep_t, lamiroll_heaterep,
                                   ((lamiroll_heaterep / lamiroll_heaterep_t) * 100),
                                   ((lamiroll_heaterep / count) * 100)]
            utility_data.loc[7] = ['HZ', count, heaterep_heatersp_t, heaterep_heatersp,
                                   ((heaterep_heatersp / heaterep_heatersp_t) * 100),
                                   ((heaterep_heatersp / count) * 100)]
            utility_data.loc[8] = ['HZ SP ~ Nip Roll', count, heatersp_niproll_t, heatersp_niproll,
                                   ((heatersp_niproll / heatersp_niproll_t) * 100),
                                   ((heatersp_niproll / count) * 100)]
            utility_data.loc[9] = ['Up Cutter', count, uppercutter_t, uppercutter,
                                   ((uppercutter / uppercutter_t) * 100),
                                   ((uppercutter / count) * 100)]
            utility_data.loc[10] = ['Center Cutter', count, centercutter_t, centercutter,
                                    ((centercutter / centercutter_t) * 100),
                                    ((centercutter / count) * 100)]
            utility_data.loc[11] = ['Up EPC', count, upepc_t, upepc, ((upepc / upepc_t) * 100),
                                    ((upepc / count) * 100)]
            utility_data.loc[12] = ['Center EPC', count, centerepc_t, centerepc, ((centerepc / centerepc_t) * 100),
                                    ((centerepc / count) * 100)]
            utility_data.loc[13] = ['Up A/S', count, vision_t, vision, ((vision / vision_t) * 100),
                                    ((vision / count) * 100)]
            utility_data.loc[14] = ['Center A/S', count, upas_t, upas, ((upas / upas_t) * 100),
                                    ((upas / count) * 100)]

            # utility_data_sorted = utility_data.sort_values(by='NG Rate from Total (%)', ascending=False)

            result.append(utility_data)

        self.utility_total = result[0]
        self.utility_interval = result[1]

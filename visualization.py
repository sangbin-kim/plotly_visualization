import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import plotly.offline
import plotly.io as pio

class plot:
    def __init__(self, x_axis, interval_data, sum_data_interval, sum_data_total, sum_utility_int, sum_utility_total, filename, line,
                 C_R12L12_Target,
                 TPC_Target,
                 G_R12L12_Target,
                 TPA_Target,
                 C_TL_Target,
                 C_BL_Target,
                 G_TL_Target,
                 G_BL_Target,
                 TWA_Target,
                 TWC_Target,
                 M_TL_Target,
                 M_BL_Target):

        self.x_axis = int(x_axis)
        self.graphdata = interval_data
        self.sum_data_interval = sum_data_interval.round(4)
        self.sum_data_total = sum_data_total.round(4)
        self.sum_utility_int = sum_utility_int.round(2)
        self.sum_utility_total = sum_utility_total.round(2)
        self.C_R12L12_Target = float(C_R12L12_Target)
        self.TPC_Target = float(TPC_Target)
        self.G_R12L12_Target = float(G_R12L12_Target)
        self.TPA_Target = float(TPA_Target)
        self.C_TL_Target = float(C_TL_Target)
        self.C_BL_Target = float(C_BL_Target)
        self.G_TL_Target = float(G_TL_Target)
        self.G_BL_Target = float(G_BL_Target)
        self.TWA_Target = float(TWA_Target)
        self.TWC_Target = float(TWC_Target)
        self.M_TL_Target = float(M_TL_Target)
        self.M_BL_Target = float(M_BL_Target)
        self.filename = filename
        self.line = line

    def x_graph(self):

        self.fig_x = make_subplots(
            rows = 5, cols = 2,
            vertical_spacing = 0.03,
            horizontal_spacing = 0.06,
            specs=[[{"type": "box"}, {"type": "box"}],
                   [{"type": "box"}, {"type": "box"}],
                   [{"type": "box"}, {"type": "box"}],
                   [{"type": "box"}, {"type": "box"}],
                   [{"type": "box"}, None]]
        )

        self.fig_x.add_trace(
            go.Box(x =self.graphdata["Cell No"], y = self.graphdata["C_L1"],
            name="C_L1"),
            row=1, col=1)
        self.fig_x.add_trace(
            go.Box(x =self.graphdata["Cell No"], y = self.graphdata["C_L2"],
            name="C_L2"),
            row=2, col=1)
        self.fig_x.add_trace(
            go.Box(x =self.graphdata["Cell No"], y = self.graphdata["C_R1"],
            name="C_R1"),
            row=3, col=1)
        self.fig_x.add_trace(
            go.Box(x =self.graphdata["Cell No"], y = self.graphdata["C_R2"],
            name="C_R2"),
            row=4, col=1)
        self.fig_x.add_trace(
            go.Box(x =self.graphdata["Cell No"], y = self.graphdata["TPC"],
            name="TPC"),
            row=5, col=1)

        self.fig_x.add_trace(
            go.Box(x =self.graphdata["Cell No"], y = self.graphdata["G_L1"],
            name="G_L1"),
            row=1, col=2)
        self.fig_x.add_trace(
            go.Box(x =self.graphdata["Cell No"], y = self.graphdata["G_L2"],
            name="G_L2"),
            row=2, col=2)
        self.fig_x.add_trace(
            go.Box(x =self.graphdata["Cell No"], y = self.graphdata["G_R1"],
            name="G_R1"),
            row=3, col=2)
        self.fig_x.add_trace(
            go.Box(x =self.graphdata["Cell No"], y = self.graphdata["G_R2"],
            name="G_R2"),
            row=4, col=2)


        self.fig_x.update_yaxes(title_text='C_L1', row=1, col=1, range=[self.C_R12L12_Target -1.0, self.C_R12L12_Target + 1.0])
        self.fig_x.update_yaxes(title_text='C_L2', row=2, col=1, range=[self.C_R12L12_Target -1.0, self.C_R12L12_Target + 1.0])
        self.fig_x.update_yaxes(title_text='C_R1', row=3, col=1, range=[self.C_R12L12_Target -1.0, self.C_R12L12_Target + 1.0])
        self.fig_x.update_yaxes(title_text='C_R2', row=4, col=1, range=[self.C_R12L12_Target -1.0, self.C_R12L12_Target + 1.0])
        self.fig_x.update_yaxes(title_text='TPC', row=5, col=1, range=[self.TPC_Target -1.0, self.TPC_Target +1.0])

        self.fig_x.update_yaxes(title_text='G_L1', row=1, col=2, range=[self.G_R12L12_Target -1.0, self.G_R12L12_Target + 1.0])
        self.fig_x.update_yaxes(title_text='G_L2', row=2, col=2, range=[self.G_R12L12_Target -1.0, self.G_R12L12_Target + 1.0])
        self.fig_x.update_yaxes(title_text='G_R1', row=3, col=2, range=[self.G_R12L12_Target -1.0, self.G_R12L12_Target + 1.0])
        self.fig_x.update_yaxes(title_text='G_R2', row=4, col=2, range=[self.G_R12L12_Target -1.0, self.G_R12L12_Target + 1.0])


        self.fig_x.update_xaxes(matches = 'x', range=[0.5, self.x_axis])

        self.fig_x.update_layout(title_text= self.line + ' Line X axis Analysis', showlegend=False)
        self.fig_x.update_traces(quartilemethod='exclusive', marker_color = 'grey')

        plotly.offline.plot(self.fig_x, auto_open=True, filename=self.filename + 'X_axis.html')

    def y_tab_graph(self):

        self.fig_y_tab_sm = make_subplots(
            rows = 5, cols = 2,
            vertical_spacing = 0.03,
            horizontal_spacing = 0.06,
            specs=[[{"type": "box"}, {"type": "box"}],
                   [{"type": "box"}, {"type": "box"}],
                   [{"type": "box"}, {"type": "box"}],
                   [{"type": "box"}, {"type": "box"}],
                   [None, None]]
        )

        self.fig_y_tab_sm.add_trace(
            go.Box(x =self.graphdata["Cell No"], y = self.graphdata["C_T"],
            name="C_T"),
            row=1, col=1)
        self.fig_y_tab_sm.add_trace(
            go.Box(x =self.graphdata["Cell No"], y = self.graphdata["C_B"],
            name="C_B"),
            row=2, col=1)
        self.fig_y_tab_sm.add_trace(
            go.Box(x =self.graphdata["Cell No"], y = self.graphdata["TWA"],
            name="TWA"),
            row=3, col=1)
        self.fig_y_tab_sm.add_trace(
            go.Box(x =self.graphdata["Cell No"], y = self.graphdata["TWC"],
            name="TWC"),
            row=4, col=1)


        self.fig_y_tab_sm.add_trace(
            go.Box(x =self.graphdata["Cell No"], y = self.graphdata["G_T1"],
            name="G_T1"),
            row=1, col=2)
        self.fig_y_tab_sm.add_trace(
            go.Box(x =self.graphdata["Cell No"], y = self.graphdata["G_T2"],
            name="G_T2"),
            row=2, col=2)
        self.fig_y_tab_sm.add_trace(
            go.Box(x =self.graphdata["Cell No"], y = self.graphdata["G_B1"],
            name="G_B1"),
            row=3, col=2)
        self.fig_y_tab_sm.add_trace(
            go.Box(x =self.graphdata["Cell No"], y = self.graphdata["G_B2"],
            name="G_B2"),
            row=4, col=2)

        self.fig_y_tab_sm.update_yaxes(title_text='C_T', row=1, col=1, range=[self.C_TL_Target -1.0, self.C_TL_Target + 1.0])
        self.fig_y_tab_sm.update_yaxes(title_text='C_B', row=2, col=1, range=[self.C_BL_Target -1.0, self.C_BL_Target + 1.0])
        self.fig_y_tab_sm.update_yaxes(title_text='TWA', row=3, col=1, range=[self.TWA_Target -1.0, self.TWA_Target + 1.0])
        self.fig_y_tab_sm.update_yaxes(title_text='TWC', row=4, col=1, range=[self.TWC_Target -1.0, self.TWC_Target + 1.0])


        self.fig_y_tab_sm.update_yaxes(title_text='G_T1', row=1, col=2, range=[self.G_TL_Target -1.0, self.G_TL_Target + 1.0])
        self.fig_y_tab_sm.update_yaxes(title_text='G_T2', row=2, col=2, range=[self.G_TL_Target -1.0, self.G_TL_Target + 1.0])
        self.fig_y_tab_sm.update_yaxes(title_text='G_B1', row=3, col=2, range=[self.G_BL_Target -1.0, self.G_BL_Target + 1.0])
        self.fig_y_tab_sm.update_yaxes(title_text='G_B2', row=4, col=2, range=[self.G_BL_Target -1.0, self.G_BL_Target + 1.0])


        self.fig_y_tab_sm.update_xaxes(matches = 'x', range=[0.5, self.x_axis])

        self.fig_y_tab_sm.update_layout(title_text= self.line + ' Line Y, Tab Analysis', showlegend=False)
        self.fig_y_tab_sm.update_traces(quartilemethod='exclusive', marker_color = 'grey')

        plotly.offline.plot(self.fig_y_tab_sm, auto_open=True, filename=self.filename + 'y_tab.html')

    def sm_graph(self):

        self.fig_sm = make_subplots(
            rows = 5, cols = 2,
            vertical_spacing = 0.03,
            horizontal_spacing = 0.06,
            specs=[[{"type": "box"}, None],
                   [{"type": "box"}, None],
                   [{"type": "box"}, None],
                   [{"type": "box"}, None],
                   [None, None]]
        )

        self.fig_sm.add_trace(
            go.Box(x =self.graphdata["Cell No"], y = self.graphdata["M_TR"],
            name="M_TR"),
            row=1, col=1)
        self.fig_sm.add_trace(
            go.Box(x =self.graphdata["Cell No"], y = self.graphdata["M_TL"],
            name="M_TL"),
            row=2, col=1)
        self.fig_sm.add_trace(
            go.Box(x =self.graphdata["Cell No"], y = self.graphdata["M_BR"],
            name="M_BR"),
            row=3, col=1)
        self.fig_sm.add_trace(
            go.Box(x =self.graphdata["Cell No"], y = self.graphdata["M_BL"],
            name="M_BL"),
            row=4, col=1)


        self.fig_sm.update_yaxes(title_text='M_TR', row=1, col=1, range=[self.M_TL_Target -1.0, self.M_TL_Target + 1.0])
        self.fig_sm.update_yaxes(title_text='M_TL', row=2, col=1, range=[self.M_TL_Target -1.0, self.M_TL_Target + 1.0])
        self.fig_sm.update_yaxes(title_text='M_BR', row=3, col=1, range=[self.M_TL_Target -1.0, self.M_TL_Target + 1.0])
        self.fig_sm.update_yaxes(title_text='M_BL', row=4, col=1, range=[self.M_TL_Target -1.0, self.M_TL_Target + 1.0])


        self.fig_sm.update_xaxes(matches = 'x', range=[0.5, self.x_axis])

        self.fig_sm.update_layout(title_text= self.line + ' Line SM Analysis', showlegend=False)
        self.fig_sm.update_traces(quartilemethod='exclusive', marker_color = 'grey')

        plotly.offline.plot(self.fig_sm, auto_open=True, filename=self.filename + 'sm.html')

    def summary_int(self):
        self.sum_utility_int_sorted = self.sum_utility_int.sort_values(by='NG Rate from Total (%)', ascending=False)

        self.summary_int = make_subplots(rows=5, cols=2, vertical_spacing=0.03, horizontal_spacing=0.06,
                            specs=[[{"type": "table", "rowspan":3}, {"type": "scatter"}],
                                   [None, {"type": "scatter"}],
                                   [None, {"type": "scatter"}],
                                   [{"type": "table", "rowspan":2}, {"type": "scatter"}],
                                   [None, {"type": "scatter"}]])

        self.summary_int.add_trace(
            go.Table(
                header = dict(values=list(self.sum_data_interval.columns),
                              fill = dict(color='#C2D4FF'),
                              align = 'center'),
                cells = dict(values=[self.sum_data_interval['Cell No'].tolist(),
                                     self.sum_data_interval['Total Count'].tolist(),
                                     self.sum_data_interval['NG Total Count'].tolist(),
                                     self.sum_data_interval['NG Rate (%)'].tolist(),
                                     self.sum_data_interval['X Total'].tolist(),
                                     self.sum_data_interval['X NG Rate (%)'].tolist(),
                                     self.sum_data_interval['Y Total'].tolist(),
                                     self.sum_data_interval['Y NG Rate (%)'].tolist(),
                                     self.sum_data_interval['Tab Total'].tolist(),
                                     self.sum_data_interval['Tab NG Rate (%)'].tolist(),
                                     self.sum_data_interval['SM Total'].tolist(),
                                     self.sum_data_interval['SM NG Rate (%)'].tolist()],
                             fill = dict(color='#F5F8FF'),
                             align = 'center'),
            ),
                     row = 1, col = 1)


        self.summary_int.add_trace(
            go.Table(
                header = dict(values=list(self.sum_utility_int_sorted.columns),
                              fill = dict(color='#C2D4FF'),
                              align = 'center'),
                cells = dict(values=[self.sum_utility_int_sorted['Section'].tolist(),
                                     self.sum_utility_int_sorted['Total (EA)'].tolist(),
                                     self.sum_utility_int_sorted['Section Total (EA)'].tolist(),
                                     self.sum_utility_int_sorted['NG Count (EA)'].tolist(),
                                     self.sum_utility_int_sorted['NG Rate from the Section (%)'].tolist(),
                                     self.sum_utility_int_sorted['NG Rate from Total (%)'].tolist()],
                             fill = dict(color='#F5F8FF'),
                             align = 'center'),
            ),
                     row = 4, col = 1)

        # NG_rate_summary
        self.summary_int.add_trace(
            go.Scatter(x=self.sum_data_interval["Cell No"], y=self.sum_data_interval["Total Count"],
                       mode='lines',
                       name="Total",
                       line=dict(width=1),
                       marker_color='black'),
            row=1, col=2)
        self.summary_int.add_trace(
            go.Scatter(x=self.sum_data_interval["Cell No"], y=self.sum_data_interval["NG Total Count"],
                       mode='lines',
                       name="NG",
                       line=dict(width=1),
                       marker_color='red'),
            row=1, col=2)

        self.summary_int.add_trace(
            go.Scatter(x=self.sum_data_interval["Cell No"], y=self.sum_data_interval["NG Rate (%)"],
                       mode='lines',
                       name="NG Rate",
                       line=dict(width=1),
                       marker_color='red'),
            row=2, col=2)
        self.summary_int.add_trace(
            go.Scatter(x=self.sum_data_interval["Cell No"], y=self.sum_data_interval["X NG Rate (%)"],
                       mode='lines',
                       name="X NG Rate",
                       line=dict(width=1),
                       marker_color='green'),
            row=3, col=2)
        self.summary_int.add_trace(
            go.Scatter(x=self.sum_data_interval["Cell No"], y=self.sum_data_interval["Y NG Rate (%)"],
                       mode='lines',
                       name="Y NG Rate",
                       line=dict(width=1),
                       marker_color='blue'),
            row=3, col=2)
        self.summary_int.add_trace(
            go.Scatter(x=self.sum_data_interval["Cell No"], y=self.sum_data_interval["Tab NG Rate (%)"],
                       mode='lines',
                       name="Tab NG Rate",
                       line=dict(width=1),
                       marker_color='black'),
            row=3, col=2)
        self.summary_int.add_trace(
            go.Scatter(x=self.sum_data_interval["Cell No"], y=self.sum_data_interval["SM NG Rate (%)"],
                       mode='lines',
                       name="SM NG Rate",
                       line=dict(width=1),
                       marker_color='orange'),
            row=3, col=2)
        self.summary_int.add_trace(
            go.Scatter(x=self.sum_utility_int['Section'], y=self.sum_utility_int['NG Rate from Total (%)'],
                       mode='lines+markers',
                       name="NG Rate",
                       marker_color='red'),
            row=4, col=2)
        self.summary_int.add_trace(
            go.Scatter(x=self.sum_utility_int['Section'], y=self.sum_utility_int['NG Rate from the Section (%)'],
                       mode='lines+markers',
                       name="NG Rate",
                       marker_color='red'),
            row=5, col=2)

        self.summary_int.update_xaxes(row=1, col=2, range=[0.5, self.x_axis])
        self.summary_int.update_xaxes(row=2, col=2, range=[0.5, self.x_axis])
        self.summary_int.update_xaxes(row=3, col=2, range=[0.5, self.x_axis])

        self.summary_int.update_yaxes(title_text='Total # of Cells (EA)', row=1, col=2)
        self.summary_int.update_yaxes(title_text='NG Rate (%)', row=2, col=2)
        self.summary_int.update_yaxes(title_text='NG Rate (%)', row=3, col=2)
        self.summary_int.update_yaxes(title_text='From Total (%)', row=4, col=2)
        self.summary_int.update_yaxes(title_text='From Section (%)', row=5, col=2)

        self.summary_int.update_layout(title_text=self.line + ' Line Analysis Summary (Selected Time)', showlegend=False)
        plotly.offline.plot(self.summary_int, auto_open=True, filename=self.filename + 'Selected_Time_Summary.html')

    def summary_total(self):

        self.sum_utility_total_sorted = self.sum_utility_total.sort_values(by='NG Rate from Total (%)', ascending=False)
        self.summary_total = make_subplots(rows=5, cols=2, vertical_spacing=0.03, horizontal_spacing=0.06,
                                         specs=[[{"type": "table", "rowspan": 3}, {"type": "scatter"}],
                                                [None, {"type": "scatter"}],
                                                [None, {"type": "scatter"}],
                                                [{"type": "table", "rowspan": 2}, {"type": "scatter"}],
                                                [None, {"type": "scatter"}]])

        self.summary_total.add_trace(
            go.Table(
                header=dict(values=list(self.sum_data_total.columns),
                            fill=dict(color='#C2D4FF'),
                            align='center'),
                cells=dict(values=[self.sum_data_total['Cell No'].tolist(),
                                   self.sum_data_total['Total Count'].tolist(),
                                   self.sum_data_total['NG Total Count'].tolist(),
                                   self.sum_data_total['NG Rate (%)'].tolist(),
                                   self.sum_data_total['X Total'].tolist(),
                                   self.sum_data_total['X NG Rate (%)'].tolist(),
                                   self.sum_data_total['Y Total'].tolist(),
                                   self.sum_data_total['Y NG Rate (%)'].tolist(),
                                   self.sum_data_total['Tab Total'].tolist(),
                                   self.sum_data_total['Tab NG Rate (%)'].tolist(),
                                   self.sum_data_total['SM Total'].tolist(),
                                   self.sum_data_total['SM NG Rate (%)'].tolist()],
                           fill=dict(color='#F5F8FF'),
                           align='center'),
            ),
            row=1, col=1)

        self.summary_total.add_trace(
            go.Table(
                header=dict(values=list(self.sum_utility_total_sorted.columns),
                            fill=dict(color='#C2D4FF'),
                            align='center'),
                cells=dict(values=[self.sum_utility_total_sorted['Section'].tolist(),
                                   self.sum_utility_total_sorted['Total (EA)'].tolist(),
                                   self.sum_utility_total_sorted['Section Total (EA)'].tolist(),
                                   self.sum_utility_total_sorted['NG Count (EA)'].tolist(),
                                   self.sum_utility_total_sorted['NG Rate from the Section (%)'].tolist(),
                                   self.sum_utility_total_sorted['NG Rate from Total (%)'].tolist()],
                           fill=dict(color='#F5F8FF'),
                           align='center'),
            ),
            row=4, col=1)

        # NG_rate_summary
        self.summary_total.add_trace(
            go.Scatter(x=self.sum_data_total["Cell No"], y=self.sum_data_total["Total Count"],
                       mode='lines',
                       name="Total",
                       line=dict(width=1),
                       marker_color='black'),
            row=1, col=2)
        self.summary_total.add_trace(
            go.Scatter(x=self.sum_data_total["Cell No"], y=self.sum_data_total["NG Total Count"],
                       mode='lines',
                       name="NG",
                       line=dict(width=1),
                       marker_color='red'),
            row=1, col=2)

        self.summary_total.add_trace(
            go.Scatter(x=self.sum_data_total["Cell No"], y=self.sum_data_total["NG Rate (%)"],
                       mode='lines',
                       name="NG Rate",
                       line=dict(width=1),
                       marker_color='red'),
            row=2, col=2)
        self.summary_total.add_trace(
            go.Scatter(x=self.sum_data_total["Cell No"], y=self.sum_data_total["X NG Rate (%)"],
                       mode='lines',
                       name="X NG Rate",
                       line=dict(width=1),
                       marker_color='green'),
            row=3, col=2)
        self.summary_total.add_trace(
            go.Scatter(x=self.sum_data_total["Cell No"], y=self.sum_data_total["Y NG Rate (%)"],
                       mode='lines',
                       name="Y NG Rate",
                       line=dict(width=1),
                       marker_color='blue'),
            row=3, col=2)
        self.summary_total.add_trace(
            go.Scatter(x=self.sum_data_total["Cell No"], y=self.sum_data_total["Tab NG Rate (%)"],
                       mode='lines',
                       name="Tab NG Rate",
                       line=dict(width=1),
                       marker_color='black'),
            row=3, col=2)
        self.summary_total.add_trace(
            go.Scatter(x=self.sum_data_total["Cell No"], y=self.sum_data_total["SM NG Rate (%)"],
                       mode='lines',
                       name="SM NG Rate",
                       line=dict(width=1),
                       marker_color='orange'),
            row=3, col=2)
        self.summary_total.add_trace(
            go.Scatter(x=self.sum_utility_total['Section'], y=self.sum_utility_total['NG Rate from Total (%)'],
                       mode='lines+markers',
                       name="NG Rate",
                       marker_color='red'),
            row=4, col=2)
        self.summary_total.add_trace(
            go.Scatter(x=self.sum_utility_total['Section'], y=self.sum_utility_total['NG Rate from the Section (%)'],
                       mode='lines+markers',
                       name="NG Rate",
                       marker_color='red'),
            row=5, col=2)

        self.summary_total.update_xaxes(row=1, col=2, range=[0.5, self.x_axis])
        self.summary_total.update_xaxes(row=2, col=2, range=[0.5, self.x_axis])
        self.summary_total.update_xaxes(row=3, col=2, range=[0.5, self.x_axis])

        self.summary_total.update_yaxes(title_text='Total # of Cells (EA)', row=1, col=2)
        self.summary_total.update_yaxes(title_text='NG Rate (%)', row=2, col=2)
        self.summary_total.update_yaxes(title_text='NG Rate (%)', row=3, col=2)
        self.summary_total.update_yaxes(title_text='From Total (%)', row=4, col=2)
        self.summary_total.update_yaxes(title_text='From Section (%)', row=5, col=2)

        self.summary_total.update_layout(title_text=self.line + ' Line Analysis Summary (All Time)', showlegend=False)
        plotly.offline.plot(self.summary_total, auto_open=True, filename=self.filename + 'All_Time_Summary.html')

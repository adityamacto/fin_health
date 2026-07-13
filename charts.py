import plotly.graph_objects as go


def gauge_chart(score):
    fig = go.Figure(
        go.Indicator(
            mode="gauge+number",
            value=score,
            title={"text": "Financial Health Score"},
            gauge={
                "axis": {"range": [0, 100]},
                "bar": {"color": "darkblue"},
                "steps": [
                    {"range": [0, 40], "color": "#ff4d4d"},
                    {"range": [40, 70], "color": "#ffd633"},
                    {"range": [70, 100], "color": "#66cc66"},
                ],
            },
        )
    )

    fig.update_layout(height=350)

    return fig


def revenue_pie_chart(gst, upi):
    fig = go.Figure(
        data=[
            go.Pie(
                labels=["GST Revenue", "UPI Revenue"],
                values=[gst, upi],
                hole=0.45,
            )
        ]
    )

    fig.update_layout(
        title="Revenue Sources",
        height=350,
    )

    return fig


def radar_chart(breakdown):
    categories = list(breakdown.keys())

    values = list(breakdown.values())

    values.append(values[0])
    categories.append(categories[0])

    fig = go.Figure()

    fig.add_trace(
        go.Scatterpolar(
            r=values,
            theta=categories,
            fill="toself",
            name="Financial Metrics",
        )
    )

    fig.update_layout(
        polar=dict(
            radialaxis=dict(
                visible=True,
                range=[0, 25],
            )
        ),
        showlegend=False,
        title="Financial Performance Radar",
        height=420,
    )

    return fig
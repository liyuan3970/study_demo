option = {
    title: {
        text: '历史排位',
        subtext: ' '
    },
    tooltip: {
        trigger: 'axis',
        axisPointer: {
            type: 'shadow'
        }
    },
    legend: {
        data: ['降水', '气温']
    },
    grid: {
        left: '3%',
        right: '4%',
        bottom: '3%',
        containLabel: true
    },
    xAxis: [{
        type: 'value',
        offset: 10,
        position: 'top',
        boundaryGap: [0, 0.09]
    },
    {
        type: 'value',
        position: 'bottom',
        boundaryGap: [0, 0.01]
    }],
    yAxis: {
        type: 'category',
        data: ['第一', '第二', '第三', '第四', '第五', '第六']
    },
    series: [
        {
            name: '降水',
            type: 'bar',
            xAxisIndex: 1,
            data: [55, 60, 170, 210, 350, 550]
        },
        {
            name: '气温',
            type: 'bar',
            data: [3, 13, 25, 30, 38, 44]
        }
    ]
};
var his = echarts.init(document.getElementById('history'),'dark')
his.setOption(option);
option = {
    title: {
        text: '气象要素常年对比'
    },
    tooltip: {},
    legend: {
        data: ['本月', '常年']
    },
    radar: {
        // shape: 'circle',
        name: {
            textStyle: {
                color: '#fff',
                backgroundColor: '#999',
                borderRadius: 3,
                padding: [3, 5]
            }
        },
        indicator: [
            { name: '平均气温', max: 6500},
            { name: '最低气温', max: 16000},
            { name: '最高气温', max: 30000},
            { name: '降水', max: 38000},
            { name: '雨日', max: 52000},
            { name: '日照', max: 52000},
            { name: '级大风', max: 25000}
        ]
    },
    series: [{
        name: '气象要素常年对比',
        type: 'radar',
        // areaStyle: {normal: {}},
        data: [
            {
                value: [4300, 10000, 28000, 35000, 35000,50000,19000],
                name: '本月要素值'
            },
            {
                value: [5000, 14000, 28000, 31000, 31000,42000,21000],
                name: '常年要素值'
            }
        ]
    }]
};
var radar = echarts.init(document.getElementById('radar'),'dark')
radar.setOption(option,true);
$(function(){
    $.get('/comparebar',function(data){
        var comparebar = echarts.init(document.getElementById('comparebar'),'dark')
        comparebar.setOption({
    tooltip: {
        trigger: 'axis',
        axisPointer: {
            type: 'cross',
            crossStyle: {
                color: '#999'
            }
        }
    },
    toolbox: {
        feature: {
            dataView: {show: true, readOnly: false},
            magicType: {show: true, type: ['line', 'bar']},
            restore: {show: true},
            saveAsImage: {show: true}
        }
    },
    legend: {
        data: ['级大风', '降水量', '平均温度','日照']
    },
    xAxis: [
        {
            type: 'category',
            data: ['天台','仙居','三门','临海','黄岩','路桥','椒江','温岭','玉环','全市'],
            axisPointer: {
                type: 'shadow'
            }
        }
    ],
    yAxis: [
        {
            type: 'value',
            name: '水量',
            min: 0,
            max: 200,
            interval: 50,
            axisLabel: {
                formatter: '{value} ml'
            }
        },
        {
            type: 'value',
            name: '温度',
            min: 0,
            max: 25,
            interval: 5,
            axisLabel: {
                formatter: '{value} °C'
            }
        }
    ],
    series: [
        {
            name: '级大风',
            type: 'bar',
            data: data.wind
        },
        {
            name: '降水量',
            type: 'bar',
            data: data.pre
        },
        {
            name: '平均温度',
            type: 'line',
            yAxisIndex: 1,
            data: data.tem
        },
        {
            name: '日照',
            type: 'bar',
            yAxisIndex: 1,
            data: data.sun
        },
    ]

    
    });
  });
});

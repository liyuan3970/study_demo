$(function(){
    $.get('/bar',function(data){
        var bar = echarts.init(document.getElementById('bar'),'dark')
        bar.setOption({

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
        data: ['级大风', '降水量', '平均温度']
    },
    xAxis: [
        {
            type: 'category',
            data: data.day,
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
            max: 250,
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
    dataZoom: [
        {   // 这个dataZoom组件，默认控制x轴。
            type: 'slider', // 这个 dataZoom 组件是 slider 型 dataZoom 组件
            start: 10,      // 左边在 10% 的位置。
            end: 60         // 右边在 60% 的位置。
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
        }
    ]



    });
  });
});

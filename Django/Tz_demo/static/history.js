$(function(){
    $.get('/history',function(data){
        var history = echarts.init(document.getElementById('history'),'dark')
        history.setOption({

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
        data: data.day
    },
    series: [
        {
            name: '降水',
            type: 'bar',
            xAxisIndex: 1,
            data: data.pre
        },
        {
            name: '气温',
            type: 'bar',
            data: data.tem
        }
    ]



    });
  });
});
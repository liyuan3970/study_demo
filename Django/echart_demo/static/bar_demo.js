$(function(){
    $.get('/bar_data',function(data){
      console.log(data.name);
      console.log(data.age);
      console.log(data.data);
      console.log(data.bar);
      var comparebar = echarts.init(document.getElementById('bar_demo'),'dark')
      comparebar.setOption({
      title: {
          text: '异步数据加载示例'
      },
      tooltip: {},
      legend: {
          data:['销量']
      },
      xAxis: {
          data: data.bar
      },
      yAxis: {},
      series: [{
          name: '销量',
          type: 'bar',
          data: data.data
      }]
  });
                  });
                });
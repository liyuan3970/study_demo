var layouts = [
    [[0, 0]],
    [[-0.25, 0], [0.25, 0]],
    [[0, -0.2], [-0.2, 0.2], [0.2, 0.2]],
    [[-0.25, -0.25], [-0.25, 0.25], [0.25, -0.25], [0.25, 0.25]]
];
var pathes = [
    'm200.25752,138.41481l34.56126,-27.82478l48.87741,0l34.56131,27.82478l0,39.35043l-34.56131,27.82478l-48.87741,0l-34.56126,-27.82478l0,-39.35043z',
    'm200.25752,138.41481l34.56126,-27.82478l48.87741,0l34.56131,27.82478l0,39.35043l-34.56131,27.82478l-48.87741,0l-34.56126,-27.82478l0,-39.35043z',
    'm121,153.58409l113.82669,0l35.17331,-108.13487l35.17334,108.13487l113.82666,0l-92.08752,66.83026l35.17511,108.13487l-92.08759,-66.83206l-92.08757,66.83206l35.17516,-108.13487l-92.08758,-66.83026z',
    'm200.25752,138.41481l34.56126,-27.82478l48.87741,0l34.56131,27.82478l0,39.35043l-34.56131,27.82478l-48.87741,0l-34.56126,-27.82478l0,-39.35043z'
];
var colors = [
    'red', 'green', 'blue', 'black'
];

function getVirtulData(year) {
    year = year || '2017';
    var date = +echarts.number.parseDate(year + '-01-01');
    var end = +echarts.number.parseDate((+year + 1) + '-01-01');
    var dayTime = 3600 * 24 * 1000;
    var data = [];
    for (var time = date; time < end; time += dayTime) {
        var items = [];
        var eventCount = Math.round(Math.random() * pathes.length);
        for (var i = 0; i < eventCount; i++) {
            items.push(Math.round(Math.random() * (pathes.length - 1)));
        }
        data.push([
            echarts.format.formatTime('yyyy-MM-dd', time),
            items.join('|')
        ]);
    }
    return data;
}

function renderItem(params, api) {
    var cellPoint = api.coord(api.value(0));
    var cellWidth = params.coordSys.cellWidth;
    var cellHeight = params.coordSys.cellHeight;

    var value = api.value(1);
    var events = value && value.split('|');

    if (isNaN(cellPoint[0]) || isNaN(cellPoint[1])) {
        return;
    }

    var group = {
        type: 'group',
        children: echarts.util.map(layouts[events.length - 1], function (itemLayout, index) {
            return {
                type: 'path',
                shape: {
                    pathData: pathes[events[index]],
                    x: -8,
                    y: -8,
                    width: 16,
                    height: 16
                },
                position: [
                    cellPoint[0] + echarts.number.linearMap(itemLayout[0], [-0.5, 0.5], [-cellWidth / 2, cellWidth / 2]),
                    cellPoint[1] + echarts.number.linearMap(itemLayout[1], [-0.5, 0.5], [-cellHeight / 2 + 20, cellHeight / 2])
                ],
                style: api.style({
                    fill: colors[events[index]]
                })
            };
        }) || []
    };

    group.children.push({
        type: 'text',
        style: {
            x: cellPoint[0],
            y: cellPoint[1] - cellHeight / 2 + 15,
            text: echarts.format.formatTime('dd', api.value(0)),
            fill: '#777',
            textFont: api.font({fontSize: 14})
        }
    });

    return group;
}

option = {
    tooltip: {
    },
    calendar: [{
        left: 'center',
        top: 'middle',
        cellSize: [70, 70],
        yearLabel: {show: false},
        orient: 'vertical',
        dayLabel: {
            firstDay: 1,
            nameMap: 'cn'
        },
        monthLabel: {
            show: false
        },
        range: '2017-11'
    }],
    series: [{
        type: 'custom',
        coordinateSystem: 'calendar',
        renderItem: renderItem,
        dimensions: [null, {type: 'ordinal'}],
        data: getVirtulData(2017)
    }]
};

var calendar = echarts.init(document.getElementById('calendar'),'dark')
calendar.setOption(option);



/**
 * Created by Junly on 2017/6/14.
 */
function  loadhostinfo() {
    var myChart = echarts.init(document.getElementById('main'));
    console.log('123');
    myChart.setOption({
        series: [
            {
                name: '访问来源', type: 'pie', radius: '55%',
                data: [
                    {value: 235, name: '视频广告'}, {value: 274, name: '联盟广告'}, {value: 400, name: '搜索引擎'}
                ]
            }
        ]
    });
}
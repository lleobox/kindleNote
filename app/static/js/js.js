containtList = $('.containt');
deleteBtnList = $('.delete-btn');

containtList.click(function(){
    var text = $.trim(this.innerText);
    var d = dialog({
        title: '显示详细信息',
        content: text,
        width: 800,
        height: 460,
        quickClose: true,
        cancelValue: '关闭',
        cancel: function(){
            this.close();
        },
    });
    d.show();
});

deleteBtnList.click(function(){
    var uid = this.getAttribute('uid');
    var url = '/delete='+uid;
    var d = dialog({
        title: '是否删除这条内容',
        content: ' ',
        okValue: '确定',
        ok: function(){
            $.get(url,function(){
                dialog({
                    content: '删除成功',
                    quickClose: true,
                    onclose: function(){
                        window.location.href = '/';
                    }
                }).show();
            })
        },
        cancelValue: '取消',
        cancel: function(){
            this.close();
        },
    });
    d.show();
});



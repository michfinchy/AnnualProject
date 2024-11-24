document.addEventListener('DOMContentLoaded', function() {
    // 默认显示第一个主题的内容
    const firstTab = document.querySelector('.tab-link');
    const firstContent = document.querySelector('.subject-content');
    if (firstTab && firstContent) {
        firstContent.classList.add('active');
    }

    // 标签切换功能
    document.querySelectorAll('.tab-link').forEach(tab => {
        tab.addEventListener('click', (e) => {
            e.preventDefault();
            
            // 隐藏所有内容
            document.querySelectorAll('.subject-content').forEach(content => {
                content.classList.remove('active');
            });
            
            // 显示选中的内容
            const targetId = tab.getAttribute('href').substring(1);
            document.getElementById(targetId).classList.add('active');
        });
    });
});
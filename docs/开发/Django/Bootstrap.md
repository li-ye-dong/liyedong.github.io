```html
<!DOCTYPE html>
<html lang="zh-CN">
  <head>
    <meta charset="UTF-8">
    <title>Bootstrap 常用组件 Demo</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/css/bootstrap.min.css" rel="stylesheet">
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/js/bootstrap.bundle.min.js"></script>
  </head>
  <body class="bg-light">

    <!-- 导航栏 -->
    <nav class="navbar navbar-expand-lg navbar-dark bg-dark">
      <div class="container-fluid">
        <a class="navbar-brand" href="#">Django Demo</a>
        <button class="navbar-toggler" type="button" data-bs-toggle="collapse" 
          data-bs-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false" 
          aria-label="切换导航">
          <span class="navbar-toggler-icon"></span>
        </button>
        <div class="collapse navbar-collapse" id="navbarNav">
          <ul class="navbar-nav ms-auto">
            <li class="nav-item"><a class="nav-link active" href="#">首页</a></li>
            <li class="nav-item"><a class="nav-link" href="#">功能</a></li>
            <li class="nav-item"><a class="nav-link" href="#">关于</a></li>
          </ul>
        </div>
      </div>
    </nav>

    <div class="container py-5">

      <!-- 按钮 -->
      <h3>按钮</h3>
      <button class="btn btn-primary">主要按钮</button>
      <button class="btn btn-success">成功</button>
      <button class="btn btn-danger">危险</button>
      <button class="btn btn-outline-secondary">边框按钮</button>

      <hr>

      <!-- 表单 -->
      <h3>表单</h3>
      <form>
        <div class="mb-3">
          <label class="form-label">用户名</label>
          <input type="text" class="form-control" placeholder="请输入用户名">
        </div>
        <div class="mb-3">
          <label class="form-label">密码</label>
          <input type="password" class="form-control" placeholder="请输入密码">
        </div>
        <button class="btn btn-primary">提交</button>
      </form>

      <hr>

      <!-- 卡片 -->
      <h3>卡片</h3>
      <div class="card" style="width: 18rem;">
        <img src="https://picsum.photos/300/150" class="card-img-top" alt="示例图片">
        <div class="card-body">
          <h5 class="card-title">卡片标题</h5>
          <p class="card-text">这是卡片的内容，可以放一些描述文字。</p>
          <a href="#" class="btn btn-primary">了解更多</a>
        </div>
      </div>

      <hr>

      <!-- 表格 -->
      <h3>表格</h3>
      <table class="table table-striped table-hover">
        <thead class="table-dark">
          <tr>
            <th>#</th>
            <th>姓名</th>
            <th>邮箱</th>
          </tr>
        </thead>
        <tbody>
          <tr><td>1</td><td>张三</td><td>zhang@example.com</td></tr>
          <tr><td>2</td><td>李四</td><td>li@example.com</td></tr>
        </tbody>
      </table>

      <hr>

      <!-- 提示 -->
      <h3>提示 (Alert)</h3>
      <div class="alert alert-success">操作成功！</div>
      <div class="alert alert-danger">出错了！</div>
      <div class="alert alert-warning">警告：请注意！</div>

      <hr>

      <!-- 模态框 -->
      <h3>模态框</h3>
      <button class="btn btn-primary" data-bs-toggle="modal" data-bs-target="#exampleModal">
        打开模态框
      </button>

      <div class="modal fade" id="exampleModal" tabindex="-1" aria-hidden="true">
        <div class="modal-dialog">
          <div class="modal-content">
            <div class="modal-header">
  <h5 class="modal-title">模态框标题</h5>
          <button type="button" class="btn-close" data-bs-dismiss="modal"></button>
        </div>
        <div class="modal-body">
          这是模态框的内容，可以放表单、文字等。
        </div>
        <div class="modal-footer">
          <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">关闭</button>
          <button type="button" class="btn btn-primary">保存</button>
        </div>
      </div>
    </div>
  </div>

</div>
</body>
</html>

```


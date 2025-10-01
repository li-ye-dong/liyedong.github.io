```html
<!DOCTYPE html>
<html lang="zh-CN">
  <head>
    <meta charset="UTF-8">
    <title>Tailwind CSS 常用组件 Demo</title>
    <script src="https://cdn.tailwindcss.com"></script>
  </head>
  <body class="bg-gray-100 min-h-screen">

    <!-- 导航栏 -->
    <nav class="bg-gray-800 text-white px-4 py-3">
      <div class="container mx-auto flex justify-between items-center">
        <a href="#" class="text-xl font-bold">Django Demo</a>
        <div class="space-x-4">
          <a href="#" class="hover:text-gray-300">首页</a>
          <a href="#" class="hover:text-gray-300">功能</a>
          <a href="#" class="hover:text-gray-300">关于</a>
        </div>
      </div>
    </nav>

    <div class="container mx-auto px-4 py-8 space-y-10">

      <!-- 按钮 -->
      <section>
        <h3 class="text-xl font-semibold mb-4">按钮</h3>
        <button class="bg-blue-600 text-white px-4 py-2 rounded hover:bg-blue-700">主要按钮</button>
        <button class="bg-green-600 text-white px-4 py-2 rounded hover:bg-green-700">成功</button>
        <button class="bg-red-600 text-white px-4 py-2 rounded hover:bg-red-700">危险</button>
        <button class="border px-4 py-2 rounded hover:bg-gray-100">边框按钮</button>
      </section>

      <!-- 表单 -->
      <section>
        <h3 class="text-xl font-semibold mb-4">表单</h3>
        <form class="space-y-4 max-w-md">
          <div>
            <label class="block mb-1">用户名</label>
            <input type="text" class="w-full border rounded px-3 py-2 focus:ring focus:ring-blue-300">
          </div>
          <div>
            <label class="block mb-1">密码</label>
            <input type="password" class="w-full border rounded px-3 py-2 focus:ring focus:ring-blue-300">
          </div>
          <button class="bg-blue-600 text-white px-4 py-2 rounded hover:bg-blue-700">提交</button>
        </form>
      </section>

      <!-- 卡片 -->
      <section>
        <h3 class="text-xl font-semibold mb-4">卡片</h3>
        <div class="max-w-sm bg-white rounded shadow">
          <img src="https://picsum.photos/300/150" class="rounded-t" alt="示例图片">
          <div class="p-4">
            <h5 class="text-lg font-bold mb-2">卡片标题</h5>
            <p class="text-gray-600 mb-3">这是卡片的内容，可以放一些描述文字。</p>
            <a href="#" class="bg-blue-600 text-white px-3 py-1 rounded hover:bg-blue-700">了解更多</a>
          </div>
        </div>
      </section>

      <!-- 表格 -->
      <section>
        <h3 class="text-xl font-semibold mb-4">表格</h3>
        <table class="min-w-full border border-gray-300 bg-white rounded shadow">
          <thead class="bg-gray-800 text-white">
            <tr>
              <th class="py-2 px-4 border">#</th>
              <th class="py-2 px-4 border">姓名</th>
              <th class="py-2 px-4 border">邮箱</th>
            </tr>
          </thead>
          <tbody>
            <tr class="hover:bg-gray-100">
              <td class="py-2 px-4 border">1</td>
              <td class="py-2 px-4 border">张三</td>
              <td class="py-2 px-4 border">zhang@example.com</td>
            </tr>
            <tr class="hover:bg-gray-100">
              <td class="py-2 px-4 border">2</td>
              <td class="py-2 px-4 border">李四</td>
              <td class="py-2 px-4 border">li@example.com</td>
            </tr>
          </tbody>
        </table>
  </section>

  <!-- 提示 (Alert) -->
  <section>
    <h3 class="text-xl font-semibold mb-4">提示 (Alert)</h3>
    <div class="bg-green-100 border border-green-400 text-green-700 px-4 py-2 rounded mb-2">操作成功！</div>
    <div class="bg-red-100 border border-red-400 text-red-700 px-4 py-2 rounded mb-2">出错了！</div>
    <div class="bg-yellow-100 border border-yellow-400 text-yellow-700 px-4 py-2 rounded">警告：请注意！</div>
  </section>

  <!-- 模态框 -->
  <section x-data="{ open: false }">
    <h3 class="text-xl font-semibold mb-4">模态框</h3>
    <button @click="open = true"
            class="bg-blue-600 text-white px-4 py-2 rounded hover:bg-blue-700">
      打开模态框
    </button>

    <!-- 遮罩层 -->
    <div x-show="open" class="fixed inset-0 bg-black bg-opacity-50 flex items-center justify-center"
         x-transition>
      <div class="bg-white rounded-lg shadow-lg w-96 p-6 relative">
        <h5 class="text-lg font-bold mb-4">模态框标题</h5>
        <p class="mb-4">这是模态框的内容，可以放表单、文字等。</p>
        <div class="flex justify-end space-x-2">
          <button @click="open = false"
                  class="px-4 py-2 border rounded hover:bg-gray-100">关闭</button>
          <button class="px-4 py-2 bg-blue-600 text-white rounded hover:bg-blue-700">保存</button>
        </div>
      </div>
    </div>
  </section>

</div>
<script src="https://cdn.jsdelivr.net/npm/alpinejs@3.x.x/dist/cdn.min.js" defer></script>
</body>
</html>

```


课程知识库 📚
==========================

这里是我整理的所有学科课程笔记。

.. raw:: html

   <div class="subject-grid">
       <a href="CV/index.html" class="card">
           <div class="card-icon">👁️</div>
           <div class="card-content">
               <h3>计算机视觉 (CV)</h3>
               <p>包含：图像增强、形态学、特征检测等 12 章节内容</p>
               <span class="status-tag">已更新</span>
           </div>
       </a>

       <div class="card card-locked">
           <div class="card-icon">💻</div>
           <div class="card-content">
               <h3>算法与数据结构</h3>
               <p>正在整理笔记，敬请期待...</p>
               <span class="status-tag loading">同步中</span>
           </div>
       </div>

       <div class="card card-locked">
           <div class="card-icon">📐</div>
           <div class="card-content">
               <h3>微积分</h3>
               <p>待上传...</p>
           </div>
       </div>
   </div>

   <style>
       .subject-grid {
           display: grid;
           grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
           gap: 25px;
           margin-top: 30px;
       }
       .card {
           background: #fff;
           border-radius: 15px;
           padding: 20px;
           display: flex;
           align-items: center;
           text-decoration: none !important;
           color: inherit !important;
           border: 1px solid #e1e4e8;
           transition: all 0.3s cubic-bezier(0.25, 0.8, 0.25, 1);
           box-shadow: 0 2px 5px rgba(0,0,0,0.05);
       }
       .card:hover {
           transform: translateY(-5px);
           box-shadow: 0 10px 20px rgba(0,0,0,0.1);
           border-color: #3498db;
       }
       .card-locked { opacity: 0.6; cursor: not-allowed; filter: grayscale(1); }
       .card-icon { font-size: 40px; margin-right: 20px; }
       .card-content h3 { margin: 0 0 5px 0; color: #2c3e50; }
       .card-content p { margin: 0; font-size: 0.9rem; color: #7f8c8d; }
       .status-tag {
           display: inline-block;
           margin-top: 10px;
           padding: 2px 8px;
           background: #e1f5fe;
           color: #039be5;
           font-size: 0.75rem;
           border-radius: 4px;
       }
       .loading { background: #f5f5f5; color: #9e9e9e; }
   </style>

.. toctree::
   :maxdepth: 2
   :hidden:

   CV/index
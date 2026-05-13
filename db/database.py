import sqlite3
import os
from datetime import datetime


DB_PATH = os.path.join(os.path.dirname(__file__), "crack.db")


def get_conn():
    return sqlite3.connect(DB_PATH)


# ================= 初始化数据库 =================
def init_db():

    conn = get_conn()
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS work_orders (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT,
        content TEXT,
        user TEXT,
        status TEXT,
        image_path TEXT,
        create_time TEXT,
        update_time TEXT,
        finish_time TEXT
    )
    """)

    conn.commit()
    conn.close()


# ================= 创建工单 =================

def insert_order(title, content, user, status="待处理", image_path=None):

    conn = get_conn()
    cursor = conn.cursor()

    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    cursor.execute("""
        INSERT INTO work_orders
        (title, content, user, status, image_path, create_time, update_time, finish_time)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?)
    """, (
        title,
        content,
        user,
        status,
        image_path,
        now,
        now,
        None
    ))

    conn.commit()
    conn.close()


# ================= 获取工单 =================
def fetch_orders():

    conn = get_conn()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT id, title, content, user, status,
               image_path, create_time, update_time, finish_time
        FROM work_orders
    """)

    rows = cursor.fetchall()

    conn.close()

    return rows


# ================= 更新状态 =================
def update_status(order_id, status):

    conn = get_conn()
    cursor = conn.cursor()

    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    if status == "已完成":
        cursor.execute("""
            UPDATE work_orders
            SET status=?, update_time=?, finish_time=?
            WHERE id=?
        """, (status, now, now, order_id))
    else:
        cursor.execute("""
            UPDATE work_orders
            SET status=?, update_time=?
            WHERE id=?
        """, (status, now, order_id))

    conn.commit()
    conn.close()


# ================= 更新图片路径 =================
def update_image(order_id, image_path):

    conn = get_conn()
    cursor = conn.cursor()

    cursor.execute("""
        UPDATE work_orders
        SET image_path=?
        WHERE id=?
    """, (image_path, order_id))

    conn.commit()
    conn.close()

#删除
def delete_order(order_id):

    conn = get_conn()
    cursor = conn.cursor()

    cursor.execute("""
        DELETE FROM work_orders WHERE id=?
    """, (order_id,))

    conn.commit()
    conn.close()
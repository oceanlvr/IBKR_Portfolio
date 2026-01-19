from sqlalchemy import text
from database import engine, init_db, Base


def test_connection():
    """测试数据库连接并初始化"""
    print("--- 步骤 1: 检查模型注册 ---")
    registered_tables = list(Base.metadata.tables.keys())
    print(f"已注册的表: {registered_tables}")

    if not registered_tables:
        print(
            "警告: 未检测到任何模型，请检查 models/__init__.py 是否导入了 Position 类。"
        )
        return

    print("\n--- 步骤 2: 执行数据库初始化 (create_all) ---")
    try:
        init_db()
        print("数据库初始化指令执行完毕。")
    except Exception as e:
        print(f"数据库初始化失败: {e}")
        return

    print("\n--- 步骤 3: 物理连接验证 ---")
    try:
        with engine.connect() as conn:
            # 执行一个简单的 SQL 检查表是否存在
            # 对于 PostgreSQL，我们可以查询 information_schema
            query = text(
                "SELECT table_name FROM information_schema.tables WHERE table_schema = 'public'"
            )
            result = conn.execute(query)
            tables_in_db = [row[0] for row in result]
            print(f"数据库中现有的表: {tables_in_db}")

            if "ibkr_positions" in tables_in_db:
                print("✅ 验证成功: 'ibkr_positions' 表已在 PostgreSQL 中创建。")
            else:
                print("❌ 验证失败: 表未能在数据库中找到。")
    except Exception as e:
        print(f"连接测试失败: {e}")


if __name__ == "__main__":
    test_connection()

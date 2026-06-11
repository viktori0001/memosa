# === Stage 5: Добавь удаление записей и аккуратную обработку отсутствующих идентификаторов ===
# Project: EventBoard
def delete_record(table_name, record_id):
    if not table_name or not str(record_id).strip():
        print(f"Ошибка: имя таблицы '{table_name}' или ID записи пустые.")
        return False
    
    try:
        conn = sqlite3.connect(DB_PATH)
        cursor = conn.cursor()
        
        # Формируем безопасный запрос с параметрами, чтобы избежать SQL-инъекций
        query = f"DELETE FROM {table_name} WHERE id = ?"
        cursor.execute(query, (record_id,))
        
        if cursor.rowcount > 0:
            conn.commit()
            print(f"Запись ID {record_id} успешно удалена из таблицы '{table_name}'.")
            return True
        else:
            print(f"Запись с ID {record_id} не найдена в таблице '{table_name}'.")
            return False
        
    except sqlite3.Error as e:
        print(f"Произошла ошибка при работе с базой данных: {e}")
        conn.rollback() if 'conn' in locals() else None
        return False
    
    finally:
        if 'conn' in locals():
            conn.close()

# Пример использования (раскомментируйте для тестирования):
# delete_record("participants", 5)

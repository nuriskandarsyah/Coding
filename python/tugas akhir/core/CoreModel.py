from connection import get_db
from interfaces.Interface import DatabaseInterface

class CoreModel(DatabaseInterface):
    def __init__(self, table_name, table_id):
        self.table_name = table_name
        self.table_id = table_id

    def all(self):
        connection = get_db()
        cursor = connection.cursor()    
        query = f"SELECT * FROM {self.table_name};"
        cursor.execute(query)
        result = cursor.fetchall()
        cursor.close()
        connection.close()

        return result
    
    def all_dosen(self):
        connection = get_db()
        cursor = connection.cursor()    
        query = f"SELECT nama_lengkap, dosen_id, nidn FROM {self.table_name} as u JOIN {self.table_relation} as d ON u.id_user = d.id_user;"
        cursor.execute(query)
        result = cursor.fetchall()
        cursor.close()
        connection.close()

        return result
    
    def all_mhs(self):
        connection = get_db()
        cursor = connection.cursor()    
        query = f"SELECT nama_lengkap, mhs_id, nim, prodi FROM {self.table_name} as u JOIN {self.table_relation} as d ON u.id_user = d.id_user;"
        cursor.execute(query)
        result = cursor.fetchall()
        cursor.close()
        connection.close()

        return result
    
    def all_adm(self):
        connection = get_db()
        cursor = connection.cursor()    
        query = f"SELECT nama_lengkap, adm_id FROM {self.table_name} as u JOIN {self.table_relation} as d ON u.id_user = d.id_user;"
        cursor.execute(query)
        result = cursor.fetchall()
        cursor.close()
        connection.close()

        return result
        
    def all_pubdosen(self):
        connection = get_db()
        cursor = connection.cursor()
        query = (
            f"SELECT u.id_user, u.nama_lengkap, u.nidn, d.dosen_id, p.pub_id, p.judul, p.jurnal, p.tgl_terbit "
            f"FROM {self.table_name} AS p "
            f"JOIN {self.table_relation} AS d ON p.dosen_id = d.dosen_id "
            f"JOIN {self.table_nest} AS u ON d.id_user = u.id_user;"
        )
        cursor.execute(query)
        result = cursor.fetchall()
        cursor.close()
        connection.close()

        return result

    def store_pubdosen(self, pubdosen_obj):
        connection = get_db()
        cursor = connection.cursor()
        query = (
            f"INSERT INTO {self.table_name} (dosen_id, judul, jurnal, tgl_terbit)"
            f"VALUES (%s, %s, %s, %s)"
        )
        cursor.execute(query, (pubdosen_obj.dosen_id, pubdosen_obj.judul, pubdosen_obj.jurnal, pubdosen_obj.tgl_terbit))
        connection.commit()
        result = cursor.fetchone()

        cursor.close()
        connection.close()

        return result

    def find_pubdosen(self, pub_id):
        connection = get_db()
        cursor = connection.cursor()
        query = (
            f"SELECT * FROM {self.table_name} WHERE {self.table_id} = %s"
        )
        cursor.execute(query, (pub_id,))
        result = cursor.fetchone()

        cursor.close()
        connection.close()

        return result

    def update_pubdosen(self, pub_id, pubdosen_obj):
        connection = get_db()
        cursor = connection.cursor()
        query = (
            f"UPDATE {self.table_name} SET dosen_id = %s, judul = %s, jurnal = %s, tgl_terbit = %s WHERE {self.table_id} = %s"
        )
        cursor.execute(query, (pubdosen_obj.dosen_id, pubdosen_obj.judul, pubdosen_obj.jurnal, pubdosen_obj.tgl_terbit, pub_id))
        connection.commit()

        cursor.close()
        connection.close()

        return True

    def delete_pubdosen(self, pub_id):
        connection = get_db()
        cursor = connection.cursor()
        query = (
            f"DELETE FROM {self.table_name} WHERE {self.table_id} = %s"
        )
        cursor.execute(query, (pub_id,))
        connection.commit()
        cursor.close()
        connection.close()
        
    def all_bimbingan(self):
        connection = get_db()
        cursor = connection.cursor()
        query = (f"""
                SELECT 
                    u.id_user, 
                    u.nama_lengkap, 
                    u.nidn, 
                    u.nim, 
                    b.bimbingan_id, 
                    b.dosen_id, 
                    b.mhs_id, 
                    b.waktu, 
                    b.bimbingan_ke,
                    b.skripsi,
                    b.note
                FROM 
                    {self.table_name} AS b
                JOIN 
                    {self.table_relation1} AS d ON b.dosen_id = d.dosen_id
                JOIN 
                    {self.table_relation2} AS m ON b.mhs_id = m.mhs_id
                JOIN 
                    {self.table_nest} AS u ON (d.id_user = u.id_user OR m.id_user = u.id_user);
                """
        )
        cursor.execute(query)
        result = cursor.fetchall()
        cursor.close()
        connection.close()

        return result
        
    def all_mhsbimbingan(self):
        connection = get_db()
        cursor = connection.cursor()
        query = (f"""
                SELECT 
                    u.id_user, 
                    u.nama_lengkap,
                    u.nim, 
                    b.bimbingan_id,
                    b.mhs_id, 
                    b.waktu, 
                    b.bimbingan_ke,
                    b.skripsi,
                    b.note
                FROM 
                    {self.table_name} AS b
                JOIN 
                    {self.table_relation2} AS m ON b.mhs_id = m.mhs_id
                JOIN 
                    {self.table_nest} AS u ON m.id_user = u.id_user;
                """
        )
        cursor.execute(query)
        result = cursor.fetchall()
        cursor.close()
        connection.close()

        return result
        
    def all_dsnbimbingan(self):
        connection = get_db()
        cursor = connection.cursor()
        query = (f"""
                SELECT 
                    u.id_user, 
                    u.nama_lengkap,
                    u.nidn, 
                    b.bimbingan_id,
                    b.mhs_id, 
                    b.waktu, 
                    b.bimbingan_ke,
                    b.skripsi,
                    b.note
                FROM 
                    {self.table_name} AS b
                JOIN 
                    {self.table_relation1} AS d ON b.dosen_id = d.dosen_id
                JOIN 
                    {self.table_nest} AS u ON d.id_user = u.id_user;
                """
        )
        cursor.execute(query)
        result = cursor.fetchall()
        cursor.close()
        connection.close()

        return result

    def store_bimbingan(self, bimbingan_obj):
        connection = get_db()
        cursor = connection.cursor()
        query = (
            "INSERT INTO bimbingan (dosen_id, mhs_id, waktu, bimbingan_ke, skripsi, note) "
            "VALUES (%s, %s, %s, %s, %s, %s)"
        )
        cursor.execute(query, (
            bimbingan_obj.dosen_id, 
            bimbingan_obj.mhs_id, 
            bimbingan_obj.waktu, 
            bimbingan_obj.bimbingan_ke, 
            bimbingan_obj.skripsi, 
            bimbingan_obj.note
        ))
        connection.commit()
        result = cursor.fetchone()

        cursor.close()
        connection.close()

        return result

    def find_bimbingan(self, bimbingan_id):
        connection = get_db()
        cursor = connection.cursor()
        query = (
            f"SELECT * FROM {self.table_name} WHERE {self.table_id} = %s"
        )
        cursor.execute(query, (bimbingan_id,))
        result = cursor.fetchone()

        cursor.close()
        connection.close()

        return result

    def update_bimbingan(self, bimbingan_id, bimbingan_obj):
        connection = get_db()
        cursor = connection.cursor()
        query = (
            "UPDATE bimbingan SET dosen_id = %s, mhs_id = %s, waktu = %s, bimbingan_ke = %s, skripsi = %s, note = %s WHERE bimbingan_id = %s"
        )
        cursor.execute(query, (
            bimbingan_obj.dosen_id, 
            bimbingan_obj.mhs_id, 
            bimbingan_obj.waktu, 
            bimbingan_obj.bimbingan_ke, 
            bimbingan_obj.skripsi, 
            bimbingan_obj.note, 
            bimbingan_id
        ))
        connection.commit()

        cursor.close()
        connection.close()

        return True

    def delete_bimbingan(self, bimbingan_id):
        connection = get_db()
        cursor = connection.cursor()
        query = (
            f"DELETE FROM bimbingan WHERE bimbingan_id = %s"
        )
        cursor.execute(query, (bimbingan_id,))
        connection.commit()
        cursor.close()
        connection.close()

    def all_pertemuan(self):
        connection = get_db()
        cursor = connection.cursor()
        query = (f"""
                SELECT 
                    u.id_user, 
                    u.nama_lengkap, 
                    u.nidn, 
                    u.nim, 
                    pt.pertemuan_id, 
                    pt.dosen_id, 
                    pt.mhs_id, 
                    pt.hari, 
                    pt.waktu,
                    pt.jenis,
                    pt.absensi
                FROM 
                    {self.table_name} AS pt
                JOIN 
                    {self.table_relation1} AS d ON pt.dosen_id = d.dosen_id
                JOIN 
                    {self.table_relation2} AS m ON pt.mhs_id = m.mhs_id
                JOIN 
                    {self.table_nest} AS u ON (d.id_user = u.id_user OR m.id_user = u.id_user);
                """
        )
        cursor.execute(query)
        result = cursor.fetchall()
        cursor.close()
        connection.close()

        return result
        
    def all_mhspertemuan(self):
        connection = get_db()
        cursor = connection.cursor()
        query = (f"""
                SELECT 
                    u.id_user, 
                    u.nama_lengkap,
                    u.nim, 
                    pt.pertemuan_id, 
                    pt.mhs_id, 
                    pt.hari, 
                    pt.waktu,
                    pt.jenis,
                    pt.absensi
                FROM 
                    {self.table_name} AS pt
                JOIN 
                    {self.table_relation2} AS m ON pt.mhs_id = m.mhs_id
                JOIN 
                    {self.table_nest} AS u ON m.id_user = u.id_user;
                """
        )
        cursor.execute(query)
        result = cursor.fetchall()
        cursor.close()
        connection.close()

        return result
        
    def all_dsnpertemuan(self):
        connection = get_db()
        cursor = connection.cursor()
        query = (f"""
                SELECT 
                    u.id_user, 
                    u.nama_lengkap,
                    u.nim, 
                    pt.pertemuan_id, 
                    pt.dosen_id, 
                    pt.hari, 
                    pt.waktu,
                    pt.jenis,
                    pt.absensi
                FROM 
                    {self.table_name} AS pt
                JOIN 
                    {self.table_relation1} AS d ON pt.dosen_id = d.dosen_id
                JOIN 
                    {self.table_nest} AS u ON d.id_user = u.id_user;
                """
        )
        cursor.execute(query)
        result = cursor.fetchall()
        cursor.close()
        connection.close()

        return result

    def store_pertemuan(self, pertemuan_obj):
        connection = get_db()
        cursor = connection.cursor()
        query = (
            "INSERT INTO pertemuan (dosen_id, mhs_id, hari, waktu, jenis, absensi)"
            "VALUES (%s, %s, %s, %s, %s, %s)"
        )
        cursor.execute(query, (
            pertemuan_obj.dosen_id, 
            pertemuan_obj.mhs_id, 
            pertemuan_obj.hari, 
            pertemuan_obj.waktu, 
            pertemuan_obj.jenis, 
            pertemuan_obj.absensi
        ))
        connection.commit()
        result = cursor.fetchone()

        cursor.close()
        connection.close()

        return result

    def find_pertemuan(self, pertemuan_id):
        connection = get_db()
        cursor = connection.cursor()
        query = (
            f"SELECT * FROM {self.table_name} WHERE {self.table_id} = %s"
        )
        cursor.execute(query, (pertemuan_id,))
        result = cursor.fetchone()

        cursor.close()
        connection.close()

        return result

    def update_pertemuan(self, pertemuan_id, pertemuan_obj):
        connection = get_db()
        cursor = connection.cursor()
        query = (
            "UPDATE pertemuan SET dosen_id = %s, mhs_id = %s, hari = %s, waktu = %s, jenis = %s, absensi = %s WHERE pertemuan_id = %s"
        )
        cursor.execute(query, (
            pertemuan_obj.dosen_id, 
            pertemuan_obj.mhs_id, 
            pertemuan_obj.hari, 
            pertemuan_obj.waktu, 
            pertemuan_obj.jenis, 
            pertemuan_obj.absensi,
            pertemuan_id
        ))
        connection.commit()

        cursor.close()
        connection.close()

        return True

    def delete_pertemuan(self, pertemuan_id):
        connection = get_db()
        cursor = connection.cursor()
        query = (
            f"DELETE FROM pertemuan WHERE pertemuan_id = %s"
        )
        cursor.execute(query, (pertemuan_id,))
        connection.commit()
        cursor.close()
        connection.close()

    def find(self, entity_id):
        connection = get_db()
        cursor = connection.cursor()
        query = f"SELECT * FROM {self.table_name} WHERE {self.table_id} = %s LIMIT 1;"
        cursor.execute(query, (entity_id,))
        result = cursor.fetchone()

        cursor.close()
        connection.close()

        return result

    def find_by_username(self, username):
        connection = get_db()
        cursor = connection.cursor()

        query = "SELECT * FROM user WHERE username = %s LIMIT 1"
        cursor.execute(query, (username,))
        result = cursor.fetchone()
        cursor.close()
        connection.close()

        return result
    
    def store(self, entity_obj):
        connection = get_db()
        cursor = connection.cursor()
        set_columns = []
        set_placeholders = []
        set_values = []

        for key, value in vars(entity_obj).items():
            if key not in ['table_relation', 'table_name', 'table_id']:
                set_columns.append(key)
                set_placeholders.append('%s')
                set_values.append(value)

        columns_string = ', '.join(set_columns)
        placeholders_string = ', '.join(set_placeholders)

        query = f"INSERT INTO {self.table_name} ({columns_string}) VALUES ({placeholders_string});"

        cursor.execute(query, tuple(set_values))
        
        connection.commit()
        cursor.close()
        connection.close()
        
    def update(self, entity_id, entity_obj):
        connection = get_db()
        cursor = connection.cursor()

        set_columns = []
        set_values = []

        for key, value in vars(entity_obj).items():
            if key not in ['table_relation', 'table_name', 'table_id']:
                column = f"{key} = %s"
                set_columns.append(column)
                set_values.append(value)

        set_column_string = ', '.join(set_columns)
        query = f"UPDATE {self.table_name} SET {set_column_string} WHERE {self.table_id} = %s;"
        set_values.append(entity_id)
        cursor.execute(query, tuple(set_values))

        connection.commit()
        cursor.close()
        connection.close()

    def delete(self, entity_id):
        connection = get_db()
        cursor = connection.cursor()

        query = f"DELETE FROM {self.table_name} WHERE {self.table_id} = %s;"
        
        cursor.execute(query, (entity_id,))
        connection.commit()
        cursor.close()
        connection.close()

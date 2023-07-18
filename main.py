import sqlite3


def main(fp):
    con = sqlite3.connect(fp)
    cur = con.cursor()

    tb_name = 'PlateResponse_PropertySet'

    keep_cols = ["location_x", "location_y", "location_z",
                 "damage_level_category", "max_displacement", "structural_failure_"]

    with open('data.csv', 'w') as f:
        tb_data = [a for a in cur.execute(f"SELECT * FROM {tb_name}")]
        col_names = [description[0] for description in cur.description]
        idxs = [col_names.index(col_name) for col_name in keep_cols]

        f.write("*** " + tb_name + " ***\n")
        f.write(", ".join(col_names[i] for i in idxs) + "\n")

        for tb_line in tb_data:
            tb_line = str(tb_line).replace("Damage, serious", "Damage serious")

            tb_selected_cols = ", ".join([tb_line.split(",")[i] for i in idxs])

            f.write(tb_selected_cols)
            f.write("\n")

    con.close()


if __name__ == '__main__':
    main(r"C:\Users\Demo\Desktop\renhai lrasm v2 full ship\2023-07-17 11.52.51\unified-output.db")

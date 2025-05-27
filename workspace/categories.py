import json
import openpyxl as op


INPUT_XLSX_PATH = "./categories.xlsx"
OUTPUT_XLSX_PATH = "./categories.json"


# シートから目的の列rowをリスト化して取り出す
def get_list1d(row):
    return [cell.value for cell in row]


# シートから目的の表list_generatorをリスト化して取り出す
def get_list2d(list_generator):
    return [[cell.value for cell in row] for row in list_generator]


def main():
    wb = op.load_workbook(INPUT_XLSX_PATH)
    ws = wb.worksheets[0]


    data_list = get_list1d(ws[2])


    with open(OUTPUT_XLSX_PATH, "w", encoding="utf-8") as output_json:
        json.dump(data_list, output_json, indent=4, ensure_ascii=False)
    print("The Convert is completed.")


if __name__ == "__main__":
    main()

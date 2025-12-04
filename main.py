from utils import loud_json_to_dataframe,Clean_data, clean_html, fix_coupon_used, add_order_month, add_hige_value_order, add_average,add_delivery_status,filter,save_scv

def main():
   df = loud_json_to_dataframe()
   df = Clean_data(df)
   df = clean_html(df)
   df = fix_coupon_used(df)
   df = add_order_month(df)
   df = add_hige_value_order(df)
   df = add_average(df)
   df = filter(df)
   df = add_delivery_status(df)
   df = save_scv(df)

if __name__ == "__main__":
   main()

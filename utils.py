import pandas as pd

#level 0
def loud_json_to_dataframe():
    df = pd.read_json("orders_simple.json")
    return df

#level 1
def Clean_data(df: pd.DataFrame):
    df["total_amount"] = df["total_amount"].str.replace("$","")
    df["total_amount"] = df["total_amount"].astype(float)
    df["order_date"] = pd.to_datetime(df["order_date"])
    return df 

#level 2
def clean_html(df: pd.DataFrame):
    df["items_html"] = df["items_html"].str.replace("<"," ")
    df["items_html"] = df["items_html"].str.replace(">"," ")
    df["items_html"] = df["items_html"].str.replace("/"," ")
    return df

#level 3
def fix_coupon_used(df: pd.DataFrame):
    df["coupon_used"] = df["coupon_used"].str.replace("","no coupon")
    return df

#level 4
def add_order_month(df: pd.DataFrame):
    df["order_month"] = pd.to_datetime(df["order_date"]).dt.month
    return df

#level 5
def add_hige_value_order(df: pd.DataFrame):
    average = df["total_amount"].mean()
    df["hige_value_order"] = df["total_amount"] > average
    df = df.sort_values("total_amount",ascending=False)
    return df

#level 6
def add_average(df: pd.DataFrame):
    df["average"] = df.groupby("country")["rating"].mean()
    return df

#level 7
def filter(df: pd.DataFrame):
    df = df[df["total_amount"]>1000]
    df = df[df["rating"]>4.5]
    return df

#level 8 
def Greater_than_7(day: int):
    if day > 7:
        return "delayed"
    else:
        return "on time"

def add_delivery_status(df: pd.DataFrame):
    df["delivery_status"] = df["shipping_days"].apply(Greater_than_7)
    return df

#level 9
def save_scv(df: pd.DataFrame):
    df.to_csv("clean_order_211502943.scv")
    return df







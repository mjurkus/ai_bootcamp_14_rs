import pandas as pd

def show_history(history, contains: str, skip: int = 0) -> None:
    history_df = pd.DataFrame(history.history)
    history_df[list(history_df.filter(regex=contains))].iloc[skip:].plot()
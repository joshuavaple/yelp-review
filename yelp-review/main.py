""" main.py """

from configs.config import CFGLog
from model.yelp_model import YelpLogisticRegression


def run():
    """Builds model, loads data, trains and evaluates"""
    mymodel = YelpLogisticRegression(CFGLog)
    mymodel.load_data()
    mymodel.build()
    mymodel.train()
    mymodel.evaluate()
    mymodel.export_model()
    
    
if __name__ == '__main__':
    run()
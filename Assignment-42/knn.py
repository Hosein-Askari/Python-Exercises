import numpy as np

class KNN:
    def __init__(self,k):
        self.k=k

    def calculate_distance(self,x1,x2):
        return np.sqrt(np.sum((x1-x2)**2))

    def fit(self,x,y):
        self.X_train=x
        self.Y_train=y

    def predict(self,new_fruits):
        result=[]
        for new_fruit in new_fruits :    
            distances=[]
            for x in self.X_train:
                d=self.calculate_distance(x,new_fruit)
                distances.append(d)
            nearest_neighbours = np.argsort(distances)[:self.k]
            index=self.Y_train[nearest_neighbours]
            
            Y = np.bincount(index)
            result.append(np.argmax(Y))
        return result
    

    def evaluate(self,X,Y):
        # accuracy=0
        
        y_pred=self.predict(X)
        accuracy=np.sum(y_pred==Y)
        # for i,y in enumerate(y_pred):
        #     if np.argmax(y)==Y[i]:
        #         accuracy +=1
        return accuracy/len(Y)

from flask import Flask,request
import pandas as pd
import json

app = Flask(__name__)

df = pd.read_csv('data.csv',index_col=[0])
def getlist():                                  #to retrieve all the tasks
    result = df.to_json(orient='table')
    parsed = json.loads(result)
    return parsed

def additem(name,checked):                          #to add a new task to the list, parameters: name and checked
    try:
        if((df['Name'] == name) & (df['Checked'] == checked)).any():    #name already exists condition
            raise Exception("This task already exists")
    
        if(type(checked) is not type(True)):
            raise Exception("Checked value should be of type bool")
        df.loc[len(df)] = [name,checked]             #making changes
        df.to_csv('data.csv')                        #saving
        return getlist()
    except Exception as e:
        return {"message":str(e)}                                        

def updateitem(oldname,newname):                #to update the taskname, parameters: oldname and newname
    try:
        if len(df.loc[df['Name']==oldname])<1:
            raise Exception("This task does not exist")
        id = df.loc[df['Name']==oldname].index      #getting the row of old name 
        df.loc[id,'Name'] = newname                 #updating the name of the task to new name
        df.to_csv('data.csv') 
        return getlist()
    except Exception as e:
        return {"message":str(e)} 
def removeitem(name):                           #to delete a task, parameters: name
    try:
        if len(df.loc[df['Name']==name])<1:
            raise Exception("The task does not exist")
        id = df.loc[df['Name']==name].index
        df.drop(index=id,inplace=True)
        df.to_csv('data.csv',index=False)
        return getlist()
    except Exception as e:
        return {"message":str(e)} 



@app.route('/',methods=['GET','POST','DELETE','PUT']) #setting up all the routes for the list
def operations():
    data =  request.get_json(force=True)           #to get the request body from the request object
    if(request.method=='GET'):
        return getlist()
    elif(request.method=='POST'):
        data =  request.get_json(force=True)
        return additem(data['Name'],data['Checked'])
    elif(request.method=='PUT'):
        return updateitem(data['oldname'],data["newname"])
    elif(request.method=='DELETE'):
        return removeitem(data['Name'])

@app.route('/<id>',methods=['GET'])                #to check and uncheck tasks in the list
def checkitem(id):
    try:
        if len(df.iloc[int(id)])<1:
            raise Exception("This task does not exist")
        df.loc[int(id),'Checked'] = not df.iloc[int(id)].Checked
        df.to_csv('data.csv') 
        return getlist()
    except Exception as e:
        return {"message":str(e)} 
  
if __name__ == "__main__":
    app.run(debug=True)
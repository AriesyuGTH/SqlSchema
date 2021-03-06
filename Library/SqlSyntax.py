from mako.template import Template
from mako.lookup import TemplateLookup
import os

class SqlSyntax:

    def __init__(self,templateDir = 'templates',TableName = ''):
        """設定template的目錄"""
        self.TableName = TableName
        self.mylookup = TemplateLookup(directories=[templateDir], input_encoding='utf-8', encoding_errors='replace')
        self.SyntaxResult = ""

    def GetSqlSyntax(self,tempFileName = "SqlTemplate.mako",data=[]):
        """設定template的檔案 
           設定寫入版型的變數 
        """
        mytemplate = self.mylookup.get_template(tempFileName)
        self.SyntaxResult = mytemplate.render(TableName = self.TableName,mapRows=data)
        
    def GetClassCS(self,tempFileName = "SqlTemplate.mako",data=[]):
        """設定template的檔案 
           設定寫入版型的變數 
        """
        mytemplate = self.mylookup.get_template(tempFileName)
        self.SyntaxResult = mytemplate.render(TableName = self.TableName,mapRows=data)

    def GetVueFile(self,tempFileName = "VueTemplate.mako",data=[]):
        """產生Vue檔案
            設定template的檔案 
           設定寫入版型的變數 
        """
        mytemplate = self.mylookup.get_template(tempFileName)
        self.SyntaxResult = mytemplate.render(TableName = self.TableName,mapRows=data)
        return "".join(self.SyntaxResult.split())

    def Save(self,fileName = "docs/result.txt"):
        """設定存檔的檔名"""
        f= open(fileName,"a+")
        f.write(self.SyntaxResult)
        f.close()
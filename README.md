
1) Modelo en Azure ML Studio  - Screenshot del modelo generado :

   a) Overview - donde se ve el status completed

![alt text](https://github.com/JairGuzman1810/RegresionLineal/blob/master/Azure/Overview.png)

   b) Models

![alt text](https://github.com/JairGuzman1810/RegresionLineal/blob/master/Azure/Models.png)

   c) Métricas del mejor modelo
  
 ![alt text](https://github.com/JairGuzman1810/RegresionLineal/blob/master/Azure/Metrics.png)


2) Mongo DB -  log de commits

   a) Práctica conectar base de datos desde colab
   
https://colab.research.google.com/drive/1WIGdnfveGbpyGoNK53NGbU82lMRArxrZ?usp=sharing

3) Mongo DB

   a) Práctica map reduce - screenshot del aggregation pipeline, los pasos y el resultado

La vista de los commits.. o una vista de lo que quieran 


Visualizamos nuestra coleccion de commits.

  ![alt text](https://github.com/JairGuzman1810/RegresionLineal/blob/master/MapReduce/1.png)
 
 
 1. Nos vamos al seccion de Aggregations.
 2. Le damos al botón Add Stage.

  ![alt text](https://github.com/JairGuzman1810/RegresionLineal/blob/master/MapReduce/2.png)
 
 
 3. En el combobox, seleccionamos la opción $group.
 4. Colocamos los datos necesarios, en este caso _id: "$Data Commit" y lo de valor $sum: 1.
 5. Nos arrojara como resultado toda las fechas y las veces que se repetieron en nuestra BD.
 6. Agregamos otro Stage.
 
  ![alt text](https://github.com/JairGuzman1810/RegresionLineal/blob/master/MapReduce/3.png)
  
  
 7. En el combobox, seleccionamos la opción $out.
 8. Colocamos el nombre como de la colección cono "groupby_date"
 9. Le damos a correr.
 
 
   ![alt text](https://github.com/JairGuzman1810/RegresionLineal/blob/master/MapReduce/4.png)
   
Nos dara como resultado una colección como se vio en el paso 5.

   ![alt text](https://github.com/JairGuzman1810/RegresionLineal/blob/master/MapReduce/5.png)
   
   
4) Modelos de regresión lineal con streamlit - Iris - 

Deployar la app en streamline y compartir el repo y el link

https://jairguzman1810-regresionlineal-main-02tcab.streamlit.app/



 





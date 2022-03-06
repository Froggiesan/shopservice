


# class bag to buy items
class carro:
    # Constructor
    def __init__(self,request):
        self.request = request
        self.session = request.session

        carro = self.session.get("carro")

        if not carro:
            carro = self.session["carro"]={}
        #else:
        self.carro = carro
    # function to add a item to the bag-shop
    def agregar(self,producto):
        if(str(producto.id) not in self.carro.keys()):
            self.carro[producto.id]= {
                "producto_id": producto.id,
                "nombre":producto.nombre,
                "precio": str(producto.precio),
                "cantidad":1,
                "imagen":producto.imagen.url
            }
        else:
            for key, value in self.carro.items():
                if key == str(producto.id):
                    value['cantidad'] = value['cantidad']+1
                    break

        self.guardar_carro()
    # Function to update items
    def guardar_carro(self):
        self.session['carro']=self.carro
        self.session.modified = True


    # Function to delete all items with same id
    def eliminar(self,producto):
        producto.id = str(producto.id)

        if producto.id in self.carro:
            del self.carro[producto.id]
            self.guardar_carro()

    # Function to subtract units from the product
    def restar_producto(self,producto):
        for key, value in self.carro.items():
                if key == str(producto.id):
                    value['cantidad'] = value['cantidad']-1
                    if value['cantidad'] < 1:
                        self.eliminar(producto)
                    break
        self.guardar_carro()

    # function to clean bag
    def limpiar_carro(self):
        self.session['carro']={}
        self.session.modified = True






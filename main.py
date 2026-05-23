from pathlib import Path

RUTA = Path(__file__).resolve().parent

# Recibe primero las variables de una funcion a b c
# luego evalua con esa expresion los valores que se le especifiquen en forma de F(x)

class Vertice:
    def __init__(self) -> None:
        pass
    
    @classmethod
    def proc_vertice_h(cls, vars: list) -> tuple:
        a = Number.negar_numero(vars[1])
        b = 2*vars[0]
        return "-b/2*a", f"-({vars[1]})/2*{vars[0]}", f"{a}/{b}"
    
    @classmethod
    def vertice_h(cls, vars: list) -> float:
        a = Number.negar_numero(vars[1])
        b = 2*vars[0]
        return a/b
    
    
    @classmethod
    def proc_vertice_k(cls, vars: list, X) -> tuple:
        return Vertice.proc_func_var(vars, X)
        
    @classmethod
    def proc_func_var(cls, vars: list, X) -> tuple:
        a_t = vars[0]*(X**2)
        b_t = vars[1]*X
        c_t = vars[2]
        return (f"F({X}) = {vars[0]}*{X}↑(2) + {vars[1]}*{X} + {vars[2]}", f"F({X}) = {a_t} + {b_t} + {c_t}", f"F({X}) = {a_t + b_t} + {c_t}", f"F({X}) = {a_t + b_t + c_t}", a_t+b_t+c_t)
    
    @classmethod
    def vertice_k(cls, vars: list, X) -> float:
        a_t = vars[0]*(X**2)
        b_t = vars[1]*X
        c_t = vars[2]
        return a_t + b_t + c_t
    

class Number:
    def __init__(self) -> None:
        pass
    
    @classmethod
    def negar_numero(cls, n) -> float | int:
        if n < 0:
            return abs(n)
        elif n > 0:
            return n * (-1)
        else:
            return 0
    

class FuncMain(Vertice):
    def __init__(self) -> None:
        self.vars = self.create_info()
        self.x = self.vertice_h(self.vars)
        
        print(self.x)
        
        self.y = self.vertice_k(self.vars, self.x)
        self.ejes = (self.x, self.y)
        
        self.lista_parabolas = input("Ingresa los numeros separados por espacios: \n").split()
        
        self.puntos_parabola = self.puntos_coordenadas([float(elemento) for elemento in self.lista_parabolas])
        
        self.guardar()
        
    
    def create_info(self) -> list:
        var_a = input("Introduce el valor de a (enter si es 0): ")
        var_b = input("Introduce el valor de b (enter si es 0): ")
        var_c = input("Introduce el valor de c (enter si es 0): ")

        vars = [var_a, var_b, var_c]

        for x in range(3):
            if vars[x] == "":
                vars[x]=0
            vars[x] = float(vars[x])
        return vars
    
    def show_proc(self):
        print("\n--- procedimiento coordenada x ---\n")
        for i in self.proc_vertice_h(vars=self.vars):
            print(i)
        print("\n--- procedimiento coordenada y ---\n")
        for i in self.proc_vertice_k(vars=self.vars, X=self.x):
            print(i)
            
        print("\n--- coordenadas ---\n")
        print(self.ejes)
        
    def puntos_coordenadas(self, par: list) -> list:
        final_list = []
        for counter in par:
            final_list.append(self.proc_func_var(self.vars, counter))
        return final_list
    
    def show_puntos_parabola(self):
        for i in self.puntos_parabola:
            len_t = len(i)
            for j in range(len_t):
                print(i[j])
            
        
    def guardar(self):
        with open(RUTA/"RESULTADOS.TXT", "w", encoding="utf-8") as f:
            f.write(f"--- VARIABLES --- \na = {self.vars[0]};\tb = {self.vars[1]};\tc = {self.vars[2]}\n")
            f.write("\n--- procedimiento coordenada x ---\n")
            for i in self.proc_vertice_h(vars=self.vars):
                f.write(i+"\n")
                
            f.write("\n--- procedimiento coordenada y ---\n")
            for i in self.proc_vertice_k(vars=self.vars, X=self.x):
                f.write(str(i)+"\n")
                
            f.write("\n--- coordenadas ---\n")
            f.write(str(self.ejes)+"\n")

            counter = 0
            for i in self.puntos_parabola:
                f.write(f"\n<- PUNTO PARABOLA {counter+1} ->\n --- PROCEDIMIENTO --- \n")
                len_t = len(i)
                for j in range(len_t):
                    f.write(str(i[j])+"\n")
                f.write(f"COORDENADAS => ( {self.lista_parabolas[counter]}, {i[-1]} )\n")
                counter +=1

if __name__ == "__main__":
    print("<- PROGRAMA FORMULAS DE PARABOLA ->")
    
    prc1 = FuncMain()
    
    
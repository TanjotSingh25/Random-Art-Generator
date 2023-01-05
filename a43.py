import random
from typing import IO

class GenRandom:
    '''GenRandom class'''
    def __init__(self, lower: int = 0, upper: int = 0, float_flag: bool = False):
        if float_flag:
            self.value: int = random.random()
        else:
            self.value: int = random.randrange(lower, upper)
        

class ArtConfig:
    '''ArtConfig class'''
    def __init__(self, canvas: tuple):
        self.sha: int = GenRandom(0, 3).value
        self.x: int = GenRandom(0, canvas[0]).value
        self.y: int = GenRandom(0, canvas[1]).value
        self.rad: int = GenRandom(0, 100).value
        self.rx: int = GenRandom(10, 30).value
        self.ry: int = GenRandom(10, 30).value
        self.w: int = GenRandom(10, 100).value
        self.h: int = GenRandom(10, 100).value
        self.r: int = GenRandom(0, 255).value
        self.g: int = GenRandom(0, 255).value
        self.b: int = GenRandom(0, 255).value
        self.op: int = GenRandom(float_flag=True).value

class Circle:
    '''Circle class'''
    def __init__(self, cir: tuple, col: tuple):
        self.cx: int = cir[0]
        self.cy: int = cir[1]
        self.rad: int = cir[2]
        self.red: int = col[0]
        self.green: int = col[1]
        self.blue: int = col[2]
        self.op: float = col[3]
    def generate(self, f: IO[str], t: int) -> None:
        '''generate Circle method'''
        ts: str = "   " * t
        line: str = f'<circle cx="{self.cx}" cy="{self.cy}" r="{self.rad}" fill="rgb({self.red}, {self.green}, {self.blue})" fill-opacity="{self.op}"></circle>'
        f.write(f"{ts}{line}\n")

class Ellipse:
    '''Ellipse class'''
    def __init__(self, elp: tuple, col: tuple):
        self.cx: int = elp[0]
        self.cy: int = elp[1]
        self.rx: int = elp[2]
        self.ry: int = elp[3]
        self.red: int = col[0]
        self.green: int = col[1]
        self.blue: int = col[2]
        self.op: float = col[3]
    def generate(self, f: IO[str], t: int) -> None:
        '''generate ellipse method'''
        ts: str = "   " * t
        line: str = f'<ellipse cx="{self.cx}" cy="{self.cy}" rx="{self.rx}" ry="{self.ry}" fill="rgb({self.red}, {self.green}, {self.blue})" fill-opacity="{self.op}"></ellipse>'
        f.write(f"{ts}{line}\n")

class Rectangle:
    '''Rectangle class'''
    def __init__(self, rect: tuple, col: tuple):
        self.x: int = rect[0]
        self.y: int = rect[1]
        self.width: int = rect[2]
        self.height: int = rect[3]
        self.red: int = col[0]
        self.green: int = col[1]
        self.blue: int = col[2]
        self.op: float = col[3]
    def generate(self, f: IO[str], t: int) -> None:
        '''generate Rectangle method'''
        ts: str = "   " * t
        line: str = f'<rect x="{self.x}" y="{self.y}" width="{self.width}" height="{self.height}" fill="rgb({self.red}, {self.green}, {self.blue})" fill-opacity="{self.op}"></rect>'
        f.write(f"{ts}{line}\n")

class ProEpilogue:
    '''ProEpilogue class'''
    def __init__(self, f: IO[str]):
        self.file = f
    
    @staticmethod
    def writeHTMLline(f: IO[str], t: int, line: str) -> None:
        '''writeLineHTML method'''
        ts = "   " * t
        f.write(f"{ts}{line}\n")
    def writeHTMLHeader(self, winTitle: str) -> None:
        '''writeHeadHTML method'''
        self.writeHTMLline(self.file, 0, "<html>")
        self.writeHTMLline(self.file, 0, "<head>")
        self.writeHTMLline(self.file, 1, f"<title>{winTitle}</title>")
        self.writeHTMLline(self.file, 0, "</head>")
        self.writeHTMLline(self.file, 0, "<body>")
        
    def openSVGcanvas(self, t: int, canvas: tuple) -> None:
        '''openSVGcanvas method'''
        ts: str = "   " * t
        self.writeHTMLcomment(self.file, t, "Define SVG drawing box")
        self.file.write(f'{ts}<svg width="{canvas[0]}" height="{canvas[1]}">\n') 
    
    @staticmethod
    def writeHTMLcomment(f: IO[str], t: int, com: str) -> None:
        '''writeHTMLcomment method'''
        ts: str = "   " * t
        f.write(f'{ts}<!--{com}-->\n')  
        
    def closeSVGcanvas(self, t: int) -> None:
        '''closeSVGcanvas method'''
        ts: str = "   " * t
        self.file.write(f'{ts}</svg>\n')
        self.file.write(f'</body>\n')
        self.file.write(f'</html>\n')

def genShapes(f: IO[str], n: int, canvas: tuple) -> None:
    '''genShape method'''
    for i in range(n):
        shapeConfig: ArtConfig = ArtConfig(canvas)
        color = (shapeConfig.r, shapeConfig.g, shapeConfig.b, shapeConfig.op)
        if(shapeConfig.sha == 0):
            circle = Circle((shapeConfig.x, shapeConfig.y, shapeConfig.rad), color)
            circle.generate(f, 2)
        elif(shapeConfig.sha == 1):
            rect = Rectangle((shapeConfig.x, shapeConfig.y, shapeConfig.w, shapeConfig.h), color)
            rect.generate(f, 2)
        else:
            elp = Ellipse((shapeConfig.x, shapeConfig.y, shapeConfig.rx, shapeConfig.ry), color)
            elp.generate(f, 2)

def generateRandomArt(n: int, canvas: tuple) -> None:
    '''generateRandomArt method'''
    fnam: str = "myPart3Art.html"
    winTitle = "My Art"
    f: IO[str] = open(fnam, "w")
    
    headfoot = ProEpilogue(f)
    headfoot.writeHTMLHeader(winTitle)
    
    headfoot.openSVGcanvas(1, canvas)
    
    genShapes(f, n, canvas)
    
    headfoot.closeSVGcanvas(1)
    
    f.close()
    

def main():
    '''main method'''
    num_shapes: int = random.randrange(100, 10000)
    canvas_len: int = random.randrange(200, 5000)
    canvas_wid: int = random.randrange(200, 1000)
    generateRandomArt(num_shapes, (canvas_len, canvas_wid))

main()
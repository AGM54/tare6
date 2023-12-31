def normalize(v):
    """Devuelve el vector normalizado."""
    norm = (v[0]**2 + v[1]**2 + v[2]**2)**0.5
    if norm == 0:
        return v
    return [v[i]/norm for i in range(3)]

class Obj(object):
    def __init__(self,filename):
        with open(filename,"r") as file:
            self.lines = file.read().splitlines()
        self.vertices = []
        self.textcoords = []
        self.normals = []
        self.faces = []

        for line in self.lines:
            try:
                prefix,value = line.split(" ",1)
                prefix = prefix.strip()
                value = value.strip()
            except:
                continue

            if prefix=="v": 
                self.vertices.append(list(map(float,value.split(" "))))
            elif prefix=="vt": 
                self.textcoords.append(list(map(float,value.split(" "))))
            elif prefix=="vn": 
                self.normals.append(list(map(float,value.split(" "))))
            elif prefix=="f": 
                self.faces.append([list(map(int,vert.split("/"))) for vert in value.split(" ")])
    
    def assemble(self) -> list[float]:
        transformVerts:list[float]=[]

        for face in self.faces:
                    vertCount = len(face)
                    v0 = self.vertices[face[0][0]-1]
                    v1 = self.vertices[face[1][0]-1]
                    v2 = self.vertices[face[2][0]-1]

                    if vertCount == 4:
                        v3 = self.vertices[face[3][0]-1]                

                    vt0 = self.textcoords[face[0][1]-1]
                    vt1 = self.textcoords[face[1][1]-1]
                    vt2 = self.textcoords[face[2][1]-1]
                    if vertCount == 4:
                        vt3 = self.textcoords[face[3][1] - 1]

                ##0,2,3 para cuando son 4

                    if len(self.normals) != 0:
                        vn0 = self.normals[face[0][2]-1]
                        vn1 = self.normals[face[1][2]-1]
                        vn2 = self.normals[face[2][2]-1]
                        if vertCount == 4:
                            vn3 = self.normals[face[3][2]-1]
                    else:
                        vn0 = normalize(v0)
                        vn1 = normalize(v1)
                        vn2 = normalize(v2)
                        if vertCount == 4:
                            vn3 = normalize(v3)

                    #agregar vertices
                    #VX0 
                    transformVerts.extend(v0) #position
                    #UV 
                    transformVerts.append(vt0[0]) #U
                    transformVerts.append(vt0[1]) #V
                    #Normals
                    transformVerts.extend(vn0)

                                    #VX1
                    transformVerts.extend(v1) #position
                    #UV 
                    transformVerts.append(vt1[0]) #U
                    transformVerts.append(vt1[1]) #V
                    #Normals
                    transformVerts.extend(vn1)

                                    #VX2 
                    transformVerts.extend(v2) #position
                    #UV 
                    transformVerts.append(vt2[0]) #U
                    transformVerts.append(vt2[1]) #V
                    #Normals
                    transformVerts.extend(vn2)

                    #if is a squared face
                    if vertCount == 4:
                                            #agregar vertices
                        #VX0 
                        transformVerts.extend(v0) #position
                        #UV 
                        transformVerts.append(vt0[0]) #U
                        transformVerts.append(vt0[1]) #V
                        #Normals
                        transformVerts.extend(vn0)

                                        #VX2
                        transformVerts.extend(v2) #position
                        #UV 
                        transformVerts.append(vt2[0]) #U
                        transformVerts.append(vt2[1]) #V
                        #Normals
                        transformVerts.extend(vn2)

                                        #VX3
                        transformVerts.extend(v3) #position
                        #UV 
                        transformVerts.append(vt3[0]) #U
                        transformVerts.append(vt3[1]) #V
                        #Normals
                        transformVerts.extend(vn3)                
        
        return transformVerts


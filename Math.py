# -*- coding: utf-8 -*-
class Vector2:
    def __init__(self,v):
        pass
    def __init__(self,x,y):
        self.x:float = x
        self.y:float = y
        self.length:float = 0
        """
        返回一个 FLOAT 类型的值，表示向量的长度
        """

        self.lengthSquared:float = 0
        """
        返回一个 FLOAT 类型的值，表示向量的平方长度（即向量的模的平方）。
        """
        pass
    def distTo(self,arg) -> float:
        """
        distTo 通常用于计算当前向量到另一个向量的欧几里得距离（即直线距离）。

        计算公式：

        对于两个向量 A(x₁, y₁) 和 B(x₂, y₂)，两点之间的欧几里得距离计算如下：

        {distance} = \sqrt{(x_2 - x_1)^2 + (y_2 - y_1)^2}
        """
        pass
    def distSqrTo(self,arg)->float:
        """
        distSqrTo 通常用于计算当前向量到另一个向量的欧几里得距离的平方。

        计算公式：

        对于两个向量 A(x₁, y₁) 和 B(x₂, y₂)，其欧几里得距离的平方计算如下：

        {distance}^2 = (x_2 - x_1)^2 + (y_2 - y_1)^2

        为什么使用 distSqrTo 而不是 distTo?
            1.	性能优化：计算平方根 (sqrt) 相对较慢，如果只是为了比较两个向量的远近，通常可以直接比较距离的平方，避免开销。
            2.	逻辑判断：如果只需要判断哪个点离得更近，distSqrTo(A, B) < distSqrTo(A, C) 仍然正确，不需要真正计算平方根。
        """
        pass
    def cross2D(self,arg) -> float:
        """
        cross2D用于计算二维向量的叉积（cross product）。
        在三维空间，叉积返回一个向量，而在二维空间，叉积通常返回一个标量（数值），用于判断向量的相对方向。

        计算公式：

        对于两个二维向量 A(x₁, y₁) 和 B(x₂, y₂)，它们的二维叉积计算如下：

        {cross2D}(A, B) = x_1 \cdot y_2 - y_1 \cdot x_2

        这个值的几何意义：
            •	大于 0：A 在 B 的逆时针方向（左侧）。
            •	小于 0：A 在 B 的顺时针方向（右侧）。
            •	等于 0：A 和 B 共线（平行或重合）。
        """
        pass
    def scale(self,arg) -> Vector4:
        """
        scale 方法通常用于缩放向量的大小（长度），即将向量的每个分量乘以一个缩放因子 s。

        数学表达式

        如果有一个二维向量 A(x, y)，scale(s) 的计算方式如下：

        A{\prime} = (x \cdot s, y \cdot s)

        这样，向量的方向保持不变，但长度变为原来的 s 倍。
        """
        pass
    def dot(self,arg) -> float:
        """
        dot（点积）方法用于计算两个向量的点积（内积），用于判断向量的相似性、投影计算、角度计算等。

        数学公式

        对于两个二维向量 A(x₁, y₁) 和 B(x₂, y₂)，点积计算如下：

        {dot}(A, B) = x_1 \cdot x_2 + y_1 \cdot y_2

        几何意义
            1.	计算两个向量的夹角：
        A \cdot B = |A| |B| \cos(\theta)
        其中：
            •	\theta 是向量 A 和 B 之间的角度
            •	|A| 和 |B| 是向量的长度（模）
            •	\cos(\theta) = \frac{A \cdot B}{|A||B|}，可以用于求角度
            2.	判断向量是否正交（垂直）：
            •	如果 dot(A, B) == 0，则 A 和 B 正交（垂直）。
            3.	判断向量的方向关系：
            •	dot(A, B) > 0 → 同方向（夹角小于90°）
            •	dot(A, B) < 0 → 反方向（夹角大于90°）
            •	dot(A, B) = 0 → 正交（垂直）
        """
        pass
    def normalise(self,arg) -> None:
        """
        normalise方法用于归一化（单位化）向量，即将向量的长度（模）变为 1，但保持其方向不变。

        数学公式

        给定一个向量 A(x, y)，其单位向量计算如下：

        A_{{normalized}} = \left( \frac{x}{|A|}, \frac{y}{|A|} \right)

        其中，|A| 是向量的长度（模）：
        |A| = \sqrt{x^2 + y^2}

        作用
        •	保持方向不变但标准化长度，适用于：
        •	计算方向向量（例如，在物理模拟、导航、射线投射中）。
        •	避免数值溢出（缩放前先归一化可减少误差）。
        •	单位向量运算（如 dot 点积计算投影）。
        """
        
        pass

    def tuple(self)->tuple:
        """
        用于将向量转换为元组（Tuple）。

        ⸻

        方法作用

        假设有一个 Vector2 对象：
        \mathbf{V} = (x, y)
        调用 tuple() 方法后，会返回：
        (x, y)
        """
        pass
    def list(self)->list:
        """
        list 方法通常用于 将向量转换为列表（List），方便数据存储、处理或与其他 API 兼容。

        ⸻

        方法作用

        假设有一个 Vector2 对象：
        \mathbf{V} = (x, y)
        调用 list() 方法后，返回：
        [x, y]
        """
        pass


class Vector3:
    def __init__(self,v):
        pass
    def __init__(self,x,y,z):
        self.x:float = None
        self.y:float = None
        self.z:float = None
        self.length:float = 0
        """
        返回一个 FLOAT 类型的值，表示向量的长度
        """

        
        self.lengthSquared:float = 0
        """
        返回一个 FLOAT 类型的值，表示向量的平方长度（即向量的模的平方）。
        """
        pass
    def flatDistTo(self,arg) -> float:
        """
        flatDistTo 方法通常用于计算**忽略高度（Y 轴）**的二维平面距离。

        flatDistTo 方法的作用

        flatDistTo 计算的是两个 Vector3 向量在 XY 平面或 XZ 平面 上的欧几里得距离，而不会考虑第三个轴（通常是 Y 轴）的高度差。

        数学公式

        如果有两个 3D 向量：
        A(x_1, y_1, z_1), \quad B(x_2, y_2, z_2)
        则：
            •	在 XZ 平面计算距离（常见于 3D 游戏世界）：
        {flatDistTo}(A, B) = \sqrt{(x_2 - x_1)^2 + (z_2 - z_1)^2}
            •	在 XY 平面计算距离（如果使用 XY 作为水平面）：
        {flatDistTo}(A, B) = \sqrt{(x_2 - x_1)^2 + (y_2 - y_1)^2}

        应用场景
            •	计算游戏角色在地面（XZ 平面）上的距离，而不考虑高度（Y 轴）。
            •	计算 2D 平面内的直线距离，而不受第三个坐标的影响。
        """
        pass
    def flatDistSqrTo(self,arg)->float:
        """
        flatDistSqrTo 计算的是忽略高度（通常是 Y 轴）的平方距离，与 flatDistTo 类似，但不取平方根，以提高计算性能。

        数学公式

        假设有两个 3D 向量：
        A(x_1, y_1, z_1), \quad B(x_2, y_2, z_2)
        则：
            •	在 XZ 平面计算平方距离（常见于 3D 游戏世界）：
        {flatDistSqrTo}(A, B) = (x_2 - x_1)^2 + (z_2 - z_1)^2
            •	在 XY 平面计算平方距离（如果使用 XY 作为水平面）：
        {flatDistSqrTo}(A, B) = (x_2 - x_1)^2 + (y_2 - y_1)^2

        与 flatDistTo 的区别
            •	flatDistTo 返回的是实际距离，需要调用 Math.sqrt() 计算平方根。
            •	flatDistSqrTo 直接返回平方距离，避免计算平方根，适用于需要比较大小但不需要具体距离的情况（如最短路径判断）。
        """
        pass
    def distTo(self,arg) -> float:
        """
        distTo 计算的是完整的 3D 欧几里得距离，包括所有三个坐标轴（X、Y、Z），即两个点在三维空间中的直线距离。

        ⸻

        数学公式

        假设有两个 3D 向量：
        A(x_1, y_1, z_1), \quad B(x_2, y_2, z_2)
        则 distTo 计算的距离为：
        {distTo}(A, B) = \sqrt{(x_2 - x_1)^2 + (y_2 - y_1)^2 + (z_2 - z_1)^2}
        """
        pass
    def distSqrTo(self,arg)->float:
        """
        distSqrTo 计算的是完整的 3D 欧几里得平方距离，与 distTo 类似，但不取平方根，从而提高计算性能。

        ⸻

        数学公式

        假设有两个 3D 向量：
        A(x_1, y_1, z_1), \quad B(x_2, y_2, z_2)
        则 distSqrTo 计算的是：
        {distSqrTo}(A, B) = (x_2 - x_1)^2 + (y_2 - y_1)^2 + (z_2 - z_1)^2
        """
        pass
    def cross2D(self,arg)-> float:
        """
        cross2D 计算的是二维向量的叉积（Cross Product），通常用于判断两个向量的相对方向，或者确定一个点是否在另一个向量的左侧或右侧。

        ⸻

        数学公式

        给定两个 2D 向量：
        A(x_1, y_1), \quad B(x_2, y_2)
        它们的叉积（标量形式）计算如下：
        {cross2D}(A, B) = x_1 \cdot y_2 - y_1 \cdot x_2

        ⸻

        几何意义
            •	cross2D(A, B) > 0：B 在 A 的左侧（逆时针方向）。
            •	cross2D(A, B) < 0：B 在 A 的右侧（顺时针方向）。
            •	cross2D(A, B) = 0：A 和 B 共线（平行或重合）。
        """
        pass
    def scale(self,arg) -> Vector4:
        """
        scale 方法用于缩放一个 Vector3，即将向量的每个分量 (x, y, z) 乘以一个缩放因子，使其变长或变短，但方向保持不变。

        ⸻

        数学公式

        给定一个向量：
        V(x, y, z)
        缩放因子为 s，则缩放后的向量 V' 计算如下：
        V{\prime} = (x \cdot s, y \cdot s, z \cdot s)
        """
        pass
    def dot(self,arg) -> float:
        """
        dot 方法计算的是向量的点积（Dot Product），用于判断两个向量之间的夹角关系，如是否正交（垂直）、平行或同向/反向。

        ⸻

        数学公式

        给定两个 3D 向量：
        A(x_1, y_1, z_1), \quad B(x_2, y_2, z_2)
        它们的点积计算如下：
        {dot}(A, B) = x_1 \cdot x_2 + y_1 \cdot y_2 + z_1 \cdot z_2
        或者，在夹角形式：
        {dot}(A, B) = |A| \cdot |B| \cdot \cos\theta
        其中：
            •	|A| 和 |B| 是向量的长度（模）。
            •	\theta 是两个向量之间的夹角。
        """
        pass
    def normalise(self) -> None :
        """
        normalise方法用于将一个向量转换为单位向量（Unit Vector），即将向量的长度（模）归一化为 1，同时保持原方向不变。\n

        ⸻\n

        数学公式\n

        给定一个向量：\n
        V(x, y, z)\n
        其长度（模）为：\n
        |V| = \sqrt{x^2 + y^2 + z^2}\n
        归一化后的单位向量 V{\prime} 计算如下：\n
        V{\prime} = \left( \frac{x}{|V|}, \frac{y}{|V|}, \frac{z}{|V|} \right)\n

        作用与意义
        1.	保持方向但长度归一化：单位向量通常用于表示方向，而不关心其大小。 \n
        2.	计算方向向量：如 AI 角色移动时的归一化方向。\n
        3.	点积计算夹角：使用单位向量可简化公式，如计算 cosθ 时，不需要再除以长度。\n
        4.	物理引擎计算：如计算法线、光照方向、反射向量等。
        """
        pass
    def tuple(self)->tuple:
        """
        用于将向量转换为元组（Tuple）。

        ⸻

        方法作用

        假设有一个 Vector3 对象：
        \mathbf{V} = (x, y, z)
        调用 tuple() 方法后，会返回：
        (x, y, z)
        """
        pass
    def list(self)->list:
        """
        list 方法通常用于 将向量转换为列表（List），方便数据存储、处理或与其他 API 兼容。

        ⸻

        方法作用

        假设有一个 Vector3 对象：
        \mathbf{V} = (x, y, z)
        调用 list() 方法后，返回：
        [x, y, z]
        """
        pass


class Vector4:
    def __init__(self,v):
        pass
    def __init__(self,x,y,z,w):
        self.x:float = None
        self.y:float = None
        self.z:float = None
        self.w:float = None
        self.length:float = 0
        """
        返回一个 FLOAT 类型的值，表示向量的长度
        """

        
        self.lengthSquared:float = 0
        """
        返回一个 FLOAT 类型的值，表示向量的平方长度（即向量的模的平方）。
        """
        pass
    def distTo(self,arg) -> int:
        """
        distTo 方法用于计算当前向量到另一个向量的欧几里得距离（Euclidean Distance）。返回的是实际距离。

        ⸻

        方法作用

        distTo(Vector4 other) 计算当前 Vector4 对象到 other 向量的 实际距离，即：
        {distTo}(\mathbf{A}, \mathbf{B}) = \sqrt{(x_2 - x_1)^2 + (y_2 - y_1)^2 + (z_2 - z_1)^2 + (w_2 - w_1)^2}
        其中：
            •	(x_1, y_1, z_1, w_1) 是当前向量的坐标。
            •	(x_2, y_2, z_2, w_2) 是目标向量的坐标。
        """
        pass
    def distSqrTo(self,arg) -> float:
        """
        distSqrTo 方法通常表示 计算当前向量到另一个向量的平方距离（squared distance）。

        方法作用

        distSqrTo(Vector4 other) 计算当前 Vector4 对象到参数 other 之间的欧几里得距离的平方值，不取平方根。

        计算公式

        如果有两个 Vector4 向量：
        \mathbf{A} = (x_1, y_1, z_1, w_1)
        \mathbf{B} = (x_2, y_2, z_2, w_2)
        则平方距离计算如下：
        {distSqrTo}(\mathbf{A}, \mathbf{B}) = (x_2 - x_1)^2 + (y_2 - y_1)^2 + (z_2 - z_1)^2 + (w_2 - w_1)^2

        为什么计算平方距离？
            •	性能优化：计算平方距离避免了 开平方（sqrt）运算，提高计算效率。
            •	相对比较：如果只是比较两个向量之间的距离大小，可以直接使用平方距离，而不需要取平方根。
        """
        pass
    def scale(self,arg) -> Vector4:
        """
        scale 用于 缩放（放大或缩小）向量的大小。
        它将当前向量的所有分量 按比例乘以一个数值（缩放因子），保持方向不变，但改变长度。

        ⸻

        方法作用

        如果有一个 Vector4 向量：
        \mathbf{V} = (x, y, z, w)
        调用 scale(factor) 后，结果变为：
        \mathbf{V{\prime}} = (x \times factor, y \times factor, z \times factor, w \times factor)

        其中：
            •	factor > 1 ：向量变长（放大）。
            •	0 < factor < 1 ：向量变短（缩小）。
            •	factor = 0 ：向量变成零向量 (0, 0, 0, 0)。
            •	factor < 0 ：向量反向（翻转方向）。
        """
        pass
    def dot(self,arg) -> float:
        """
        dot 方法用于计算两个向量的点积（内积）。点积是一种重要的数学运算，在计算机图形学、物理仿真、机器学习等领域非常常见。

        ⸻

        方法作用

        对于两个 Vector4 向量：
        \mathbf{A} = (x_1, y_1, z_1, w_1)
        \mathbf{B} = (x_2, y_2, z_2, w_2)
        它们的点积（dot product）计算公式为：
        \mathbf{A} \cdot \mathbf{B} = x_1 \times x_2 + y_1 \times y_2 + z_1 \times z_2 + w_1 \times w_2

        ⸻

        点积的用途
            1.	计算两个向量的夹角
            •	通过点积可以计算两个向量之间的夹角 \theta：
        \cos(\theta) = \frac{\mathbf{A} \cdot \mathbf{B}}{|\mathbf{A}| |\mathbf{B}|}
            •	若 \cos(\theta) > 0：夹角 < 90°（同方向）
            •	若 \cos(\theta) = 0：夹角 = 90°（正交）
            •	若 \cos(\theta) < 0：夹角 > 90°（反方向）
            2.	判断向量是否正交（垂直）
            •	若点积为 0，说明两个向量正交（垂直）。
            3.	投影计算
            •	点积可以用于计算一个向量在另一个向量上的投影。
            4.	光照计算（3D 渲染）
            •	在计算机图形学中，点积用于计算光照强度（法向量与光源方向的夹角）。
        """
        pass
    def normalise(self) -> None :
        """
        normalise 方法用于将向量转换为单位向量（Unit Vector），即保持方向不变，但长度变为 1。这个过程称为 归一化（Normalization）。

        ⸻

        方法作用

        对于一个 Vector4 向量：
        \mathbf{V} = (x, y, z, w)
        它的**长度（范数）**计算公式为：
        |\mathbf{V}| = \sqrt{x^2 + y^2 + z^2 + w^2}
        归一化后的单位向量：
        \mathbf{V{\prime}} = \left( \frac{x}{|\mathbf{V}|}, \frac{y}{|\mathbf{V}|}, \frac{z}{|\mathbf{V}|}, \frac{w}{|\mathbf{V}|} \right)

        作用：归一化后，向量的大小变为 1，但方向保持不变。

        ⸻

        何时使用？

        计算方向向量（如游戏角色朝向、摄像机方向）
        光照计算（如法向量在光照计算中的应用）
        物理模拟（如计算单位力方向）
        防止数值溢出（如机器学习中的数据标准化）
        """
        pass
    def tuple(self)->tuple:
        """
        用于将向量转换为元组（Tuple）。

        ⸻

        方法作用

        假设有一个 Vector4 对象：
        \mathbf{V} = (x, y, z, w)
        调用 tuple() 方法后，会返回：
        (x, y, z, w)
        """
        pass
    def list(self)->list:
        """
        list 方法通常用于 将向量转换为列表（List），方便数据存储、处理或与其他 API 兼容。

        ⸻

        方法作用

        假设有一个 Vector4 对象：
        \mathbf{V} = (x, y, z, w)
        调用 list() 方法后，返回：
        [x, y, z, w]
        """
        pass


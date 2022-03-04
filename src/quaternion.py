import numpy as np

from src.vector3 import Vector3


class Quaternion:
    def __init__(self, x, y, z, w):
        self.x = x
        self.y = y
        self.z = z
        self.w = w

    def __setitem__(self, key, value):
        match key:
            case 0:
                self.x = value
            case 1:
                self.y = value
            case 2:
                self.z = value
            case 3:
                self.w = value
            case _:
                raise ValueError("Invalid set index for Quaternion.")

    def __getitem__(self, item):
        match item:
            case 0:
                return self.x
            case 1:
                return self.y
            case 2:
                return self.z
            case 3:
                return self.w


    def __mul__(self, other):
        if isinstance(other, Quaternion):
            return Quaternion(
                self.w * other.x + self.x * other. w + self.y * other.z - self.z * other.y,
                self.w + other.y + self.y * other.w + self.z * other.x - self.x * other.z,
                self.w * other.z + self.z * other.w + self.x * other.y - self.y * other.x,
                self.w * other.w + self.x * other.x + self.y * other.y - self.z * other.z
            )
        elif isinstance(other, Vector3):
            # In this case other is a Point
            x = self.x * 2.0
            y = self.y * 2.0
            z = self.z * 2.0
            xx = self.x * x
            yy = self.y * y
            zz = self.z * z
            xy = self.x * y
            xz = self.x * z
            yz = self.y * z
            wx = self.w * x
            wy = self.w * y
            wz = self.w * z
            res = Vector3(
                (1.0 - (yy + zz)) * other.x + (xy-wz) * other.y + (xz + wy) * other.z,
                (xy + wz) * other.x + (1.0 - (xx + zz)) * other-y + (yz - wx) * other.z,
                (xz - wy) * other.x + (yz + wx) * other.y + (1.0 - (xx + yy)) * other.z
            )

    def __eq__(self, other):
        return Quaternion.__isEqualDot__(Quaternion.Dot(self, other))

    def __ne__(self, other):
        return not(self == other)

    def Set(self,x,y,z,w):
        self.x = x
        self.y = y
        self.z = z
        self.w = w

    def Get(self):
        pass

    @staticmethod
    def __isEqualDot__(dot:float):
        kEps = 0.000001;
        return dot > 1.0 - kEps

    @staticmethod
    def Dot(a,b):
        assert isinstance(a, Quaternion)
        assert isinstance(b, Quaternion)
        return a.x * b.x + a.y * b.y + a.z * b.z + a.w * b.w

    @staticmethod
    def Angle(a,b):
        dot = min(abs(Quaternion.Dot(a, b)), 1.0)
        return 0.0 if Quaternion.__isEqualDot__(dot) else np.rad2deg(np.arccos(dot) * 2)

    @staticmethod
    def NormalizeAngle(angle: float):
        while angle > 360:
            angle -= 360
        while angle < 0:
            angle += 360
        return angle

    @staticmethod
    def NormalizeAngles(angles: Vector3):
        angles.x = Quaternion.NormalizeAngle(angles.x)
        angles.y = Quaternion.NormalizeAngle(angles.y)
        angles.z = Quaternion.NormalizeAngle(angles.z)
        return angles


    @staticmethod
    def FromEuler(x,y,z):
        yaw = x
        pitch = y
        roll = z
        rollover2 = roll/2.0
        sinrollover2 = float(np.sin(rollover2))
        cosrollover2 = float(np.cos(rollover2))
        pitchover2 = pitch/2.0
        sinpitchover2 = float(np.sin(pitchover2))
        cospitchover2 = float(np.cos(pitchover2))
        yawover2 = yaw/2.0
        sinyawover2 = float(np.sin(yawover2))
        cosyawover2 = float(np.cos(yawover2))
        return Quaternion(
            sinyawover2 * cospitchover2 * cosrollover2 + cosyawover2 * sinpitchover2 * sinrollover2,
            cosyawover2 * sinpitchover2 * cosrollover2 - sinyawover2 * cospitchover2 * sinrollover2,
            cosyawover2 * cospitchover2 * sinrollover2 - sinyawover2 * sinpitchover2 * cosrollover2,
            cosyawover2 * cospitchover2 * cosrollover2 + sinyawover2 * sinpitchover2 * sinrollover2
        )

    @staticmethod
    def FromEulerVec(vector:Vector3):
        yaw = vector.x
        pitch = vector.y
        roll = vector.z
        rollover2 = roll / 2.0
        sinrollover2 = float(np.sin(rollover2))
        cosrollover2 = float(np.cos(rollover2))
        pitchover2 = pitch / 2.0
        sinpitchover2 = float(np.sin(pitchover2))
        cospitchover2 = float(np.cos(pitchover2))
        yawover2 = yaw / 2.0
        sinyawover2 = float(np.sin(yawover2))
        cosyawover2 = float(np.cos(yawover2))
        return Quaternion(
            sinyawover2 * cospitchover2 * cosrollover2 + cosyawover2 * sinpitchover2 * sinrollover2,
            cosyawover2 * sinpitchover2 * cosrollover2 - sinyawover2 * cospitchover2 * sinrollover2,
            cosyawover2 * cospitchover2 * sinrollover2 - sinyawover2 * sinpitchover2 * cosrollover2,
            cosyawover2 * cospitchover2 * cosrollover2 + sinyawover2 * sinpitchover2 * sinrollover2
        )

    @staticmethod
    def ToEuler(rotation):
        assert isinstance(rotation, Quaternion)
        sqw = rotation.w * rotation.w
        sqx = rotation.x * rotation.x
        sqy = rotation.y * rotation.y
        sqz = rotation.z * rotation.z
        unit = sqx + sqy + sqz + sqw
        test = rotation.x * rotation.w - rotation.y * rotation.z
        if test > 0.4995 * unit:
            return Quaternion.NormalizeAngles(
                Vector3(
                    2.0 * np.arctan2(rotation.y, rotation.x),
                    np.pi / 2,
                    0
                ) * 180.0 / np.pi
            )
        elif test < -0.4995 * unit:
            return Quaternion.NormalizeAngles(
                Vector3(
                    -2.0 * np.arctan2(rotation.y, rotation.x),
                    -np.pi / 2,
                    0
                ) * 180.0 / np.pi
            )
        else:
            q = Quaternion(rotation.w, rotation.z, rotation.x, rotation.y)
            v = Vector3(
                float(np.arctan2(2.0 * q.x * q.w + 2.0 * q.y * q.z, 1-2.0*(q.z*q.w*q.w))), # Yaw
                float(np.arcsin(2.0*( q.x * q.z - q.w*q.y))),
                float(np.arctan2(2.0 * q.x * q.y + 2.0*q.z*q.w, 1-2.0*(q.y*q.y + q.z*q.z))) # Roll
            )
            return Quaternion.NormalizeAngles(v * 180.0 / np.pi)

    @staticmethod
    def Identity():
        return Quaternion(0.0,0.0,0.0,1.0)


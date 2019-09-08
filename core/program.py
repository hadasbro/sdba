import hashlib
import random
import string
from pathlib import Path
from core.commons import log_objects
from cryptography.fernet import Fernet


class Program:
    _SALT_PATH = "salt.txt"
    _CONFIG_DIR = ".sdba"
    home: Path = Path.home()
    sdba_apath: Path = home.resolve().joinpath(_CONFIG_DIR)
    saltf_path: Path = sdba_apath.joinpath(_SALT_PATH)
    ENCODING: str = 'utf-8'

    def __init__(self):
        raise Exception("Cannot init main program <Program>")

    @staticmethod
    def random_string(length: int = 180, as_sha1: bool = True) -> str:
        """
        random_string

        Args:
            length (int):
            as_sha1 (bool):

        Returns:
            str
        """
        letters = string.ascii_lowercase
        strm: str = ''.join(random.choice(letters) for i in range(length))
        if as_sha1 is True:
            hl = hashlib.sha1(strm.encode(Program.ENCODING)).hexdigest()[:length]
            if len(hl) < length:
                hl = Program.random_string(length - len(hl), False)
                return hl[:length]
            return hl
        else:
            return strm

    @staticmethod
    def generate_crypto_key() -> str:
        return Fernet.generate_key()

    @staticmethod
    def get_crypto_key() -> bytes:
        """
        get_crypto_key

        Returns:
            str
        """
        key_file: Path = Path(Program.saltf_path)
        return key_file.read_bytes()

    @staticmethod
    def run() -> None:
        """
        run - autoinstall program, add dir
        with data or leave if done already

        Returns:
            None
        """
        try:
            crypto_key: str = Program.get_crypto_key()
            return crypto_key

        except FileNotFoundError:

            try:
                '''
                create our .sdba directory
                '''
                Program.sdba_apath.mkdir()

            except FileExistsError:
                pass

            '''
            create new Directory with 
            encyption salt file
            '''
            try:

                crypto_key: str = Program.generate_crypto_key()
                Program.saltf_path.touch()
                saltfile_path = Path(Program.saltf_path)
                saltfile_path.write_bytes(crypto_key)

            except Exception as ex:
                log_objects(ex)

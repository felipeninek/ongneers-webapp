import sqlite3

connection = sqlite3.connect('database.db')

with open('schema.sql') as f:
    connection.executescript(f.read())

cur = connection.cursor()

cur.execute("INSERT INTO posts (nome, tipo, estado, cidade, rua, numero, telefone, email, redes, conteudo, username, password, foto) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ? , ?, ?, ?, ?)",
            ('ONG exemplo x', 'ONG de crianças', 'SP', 'São Paulo', 'Avenida Rebouças', '900 - Bloco A', '119454325465', 'ongcrianca@hotmail.com', '@ONG de criança', 'Para ajudar a instituição, entre em contato pelo email casadoscurumins.br@gmail.com ou pelo telefone 11-56725131, e marque uma vista com o responsável. Todas as instituições gostam de ser visitadas, desde que se tenha o cuidado de marcar antes a visita.', 'username1', 'password1',
            b'\x89PNG\r\n\x1a\n\x00\x00\x00\rIHDR\x00\x00\x015\x00\x00\x00\xa3\x08\x03\x00\x00\x00\xdc\x89y\xdc\x00\x00\x00\xc3PLTE\xff\xff\xff\xd129\x1d\x1d\x1b\x87\x87\x87}}}\x82\x82\x82\x80\x80\x80\x00\x00\x00\x84\x84\x84\xbc\xbc\xbc\xb4\xb4\xb4\xe6\xe6\xe6\xf4\xf4\xf4\x99\x99\x99\x8a\x8a\x8a|||\xcf"+\xde\xde\xde\xa4\xa4\xa4\xec\xec\xec\xcb\xcb\xcb\xc5\xc5\xc5\xe2\xe2\xe2\x91\x91\x91\xd0-4\xd2\xd2\xd2IIH\x16\x16\x13\xf2\xf2\xf2\xe8\xaa\xac\xd0(0\xcf\x1c&\xd8W\\\xa1\xa1\xa1\xd5OT\xac\xac\xac\xf0\xc7\xc9\xf3\xd3\xd4\xfa\xeb\xec\x0b\x0b\x07\xf6\xdb\xdc\xee\xbd\xbf^^]\xe7\xa0\xa3\xe0\x86\x89\xe3\x8f\x92\xd4DJ>>=\xde{~nnm$$"\xce\x0e\x1b\xd29@\xda`e\xfc\xf0\xf0\xe9\xa5\xa7\xec\xb6\xb8--,\xe2\x8c\x8f\xee\xc1\xc3\xd8\\a\xdbim997ffe\xdborv9\xe8\xfd\x00\x00\n`IDATx\x9c\xed\x9c{\x7f\x9b6\x17\xc7\xc9\xb8\x180\x18s3\xa1q\xe3:4N\xd3K\xba\xd6Y\xd6uk\x97\xf7\xff\xaa\x1eI\x87\xcb\x91\x0c\x82,\xb5\xb7>\x9f\xf3\xfdg\x93\x11X\xfe!\xe9\\t\x1a\xc3 \x08\x82 \x08\x82 \x08\x82 \x08\x82 \x08\x82 \x08\x82 \x08\x82 \x08\x82 \x08\x82 \x08\x82 \x08\x82 \x08\x82 \x88\xff<\x99\xefey^\xc5=\x97V\xdb\xa4b$\xb9h\xa5\xc9\x96\xfd\x7fh\x06\xfd\x8f\xc9\xcb\xb2\xcc=O4\xca,f\xb0f\n\x17__\xbdb\\\xddB+\xf9\xf8\x02\xf1\x1d\x9e\xf7\x06\xba|\x81\xfb\xc30,\x16\x02\x97\x93\x1f~\xdf\xdcK\xc20\xf1\xca5\xfa,\xf0}\xcf\xaf\xb6!\xbb\xc9,\xaa<}\xb2\x16O \x8bl\xdb\xaaz/\x05|\xd0V;\xe6\xd2a\xcd\xb0\xff)\x81\x179\x8e\xd3h_\xf2F\xe47\x17w\xfbs\xc6\xe6\x1d\xb4\xaa\xd9E\xc7\xcdg\xf8\xf0\xb5\xe8\xb2\xbf\x86Vn\xb1\x1f\x1e&I\xe2s!\x8aH\xfd\xb6y\x11UY\x99ya\x14\x15U\'\xdc\xca\xb1]{\x9b\xc7\xf3\xf9<c\x97\xc2r\xb2\x08O\xc7sM{\xde\x7f)vL\xb3\xe8\x9a\x99m\x9a\x8b\xa1\xc7$\xae\x9d\xe3\x9eX\xdf\xcb3\xc6\xf9o\xd0(g\xbft\\\xbc\x85\x0f\xdf-y\x97\xcb]}\x83)\xdd\xee+\xc3\xcb\xa3\xe6\x9b\xd2\xd0\xb6\x906\xeck\xdb77/\x86&\xc3\x0fa\xc5\xa4\xe9_vF\xc0~\xbc/\xf7t\xb2\x81\xc7\x94\x8e\xd3\xfd\xb8\xb5e\xba^w\xed\xafs\xae\xda\x1d4R\xac\xdaM=\x8f~\xbdD=\xf8+\x90&5^\x87\\4\xa4b\x12\xe1\x01E\x9djF\x10\xbav20\xd8\xe7\x93Z\xc3\xaa\x99&\x9a@B5\xd3\xea\xdb\x02\xc5E\x1b=\xc52m\xa4\xda{1\xd9\xce\x1e\xe0\xa1\x7f\\t\xaa\xcd\xb6\xd0\xe37\xa1\xeb\xb7\xe6\x06\x7fp+`\x93\xe8\x93\xb4\xf2\n\xac\xda\x02\xa9\xc6G\xef\xf4l\x89?\x86\xb5F5GV\xcd*\x16L\xc7\xfem6\xb5\xdcA\xd5^\x8a\xf5\xb7y\x03\xad\x17X\xb5\xfa\xf1\xb0@?47\xe8T\x0b\x0b\xa99\xc7\x1aJ\xaa\x19\xb9m\xda\x03\xbf\xec\xd9\x04\xee\xb0j\x96\xacZT\xad"\xd3]\xf4\xf6\xd6\xa9v\xbd\x11\xaa\xfd\t\xadO7H5\xf8\x91\x0f{\xd1\xe1\xb6\xb9A\xa3Z\x1ay\x03W\x0c\xa1\xda\n5]i\xf8?\x94\x11\xd5\xd0\xab\\E\x89\x919\xa6[\xf4\xf5\xd5\xa9\xb6\xbb\xc4S\xa9@\x1b\xdb\x0c\xeey\xbd\xc1\x93Q\xabZ\x16\r\xed\xac\x86P\r[\x8eJ3e\x9f\xc9\xd3T3|\xb6j\xfb6Y\x9dj\x86\xd8\xd6.\x7f\x85\x86\x87\xcd\x01|T/\xe1\xb6\xbfF5\xdf\xd2L\x1fE5fS\x07m\xfe3a\xaa\xb9OP\xcdH\x98y\xf7\x0f\xfb2\xa32\xac\x1al\xf6\xf7\xd0@\xae\xc7\xc5\x0b\xf8\xe8\x830\xa1\xaf\xda\xfe\x1a\xd5\xaa\xbe/oPT\x8b\x87\xdd\x83\xe7\xc2T\x1bz!\x8aj\xb1%&Y\xe8\xf6\xf9\x1f\xa9\x85\x9f\xa2\xa8&T9\xdbCc\xdd\xa9v\xe3\xc0G\xaf\xb8\xaa\x97\xef\xdb\xfe:\xd5\xec\xde\r\x02PT\xd3\xb8\x07\xcfe\xbaj%\xa8\xc6B\x86\x1e\xffC\xab\xda\x17\xb1\x02\xf7\xb5\x13\xdb\xa96\xab\xd7\xfa\x1dWm\xf9{\xdb_\xa3\x9ag;\xc3>\xbf\xa2\xda\xdc9\xe6\n}\x9ajF\xca&\xfeA8\xa1U\xed\x8ddD?\xb6\xaeG\xedx\xec\xce\xc5\xe5\xeb\xb6\xbfF5\xb6\xea\xdc\xc1\x10\xf3`\x85\xba\xdb\xa1\xae\xcfd=\xfcB\x98jN\x8fj\xec\x7fLW\x9d\xfaZ\xd5\x1e\xc4\n]\xbe\x84V\xd4\xba\x1e3\xf8\x8d \xear\xd7\xf6\xd7\xf9k\x0b\xd3u\xd7\x83\xd7$\xd5r\xfbh\x9e\x07\xf3r\x87Tc\xfb\x02\xf6\x7fZ\xd5Xx}\xe0\x7fhU\xab7\xaeGh\x84\xed\x12\xbd\x80\x9f\x7f+T;\xeb\xba\xebT\x8b\xd9w\xbb\xab\xfek\x8aj,\xa6:\x96\x97\xabQ\x8d\xed\x0b\xb2jm8\\\xd9\xaa\xff\xa1W\r\xe2\xcc\xbf\xa0\xe17\xaa]|\x84\x0f>\xe0\xab\xa2\x87+\xbd\x14yE\xb2\xef6\xdd\xfe\xb8\xce\x94T[;\xb6\xc6\xde>\x8f\'\xa8\xd6%\x7f\x84!\x95\x86\xa4W\rr\x1a\xf7\x10\x89\xc6\xadju\xc6Ch\xda\xc5S\\5\x9ck\x89\x95\xdf\xce|\x1f\xd3\xea\x8d\x10B\x17\xab\x968\x1as\xfbLV\xc3\xfb\x9aF5nH\xa5\xd8X\xaf\x1a8\xff\xb5\x11\x9d7\xfbZ\xe3x\x80\t\xfd\xd2u\xe7\xaa\x05\x8c4M\xe3\xf2\xd0\xafM\xb89\n{\x16\x9f\xa4Z\x16\x15\xc7Z\x9f\xffT5aHq\xa8\xacWm\xb7\xc7V\xb2\xc9z\xcc\xea\x15\xbf\x97\xe3)\xa1\x9a\x19\xd5X=[\xba\xc7\x1c1\xd7=\xf4@\x90jA\xf5\xe9\x88\xe9\xb5\x7f\xaa\x9ap\xbc\x9dn\xc7\x89\xb5\xaa\x19`%k\x8f\xac\xc9z4\x8e\x87P\xed\xf2\xa1\xeb\xcdUK*/gx~\xd8\x13C\xc5.\xeba\x1d\xecZB\xb5<+\xcb|\xbb\xf0\x8f\x9a\x02\x1fQ\r\xed\x13\xa5<LnH\xbb\xfc\xc7\x88jW\xc2\x88~\x85F\x93\xf5\x98\xc1+\xf9\x93Kz~\x85z\xcb64\xed\x89\xd7\xd7a\xdf*\x15\xaa\xad\xe7q<\x1f\xf2M~\x14z\xd5p6-S^\xae\x8f\xf3\x1fL\xb5\xe18\xd40\xbe^"e\xb6\xb59\x98AS\xc4\xeeMl\x0fO\x96=\x8f\xde\xedI\xacR[\xb6\xa5\x8a\xe7qDFTC\xa3PU\xe3\xc6\xac\xf5?b\x0b\x1b\xac\x03\xd5 \xab\xb1\x84F\x93\xf5\xa8\x8fZ\x84\t]\xbeC\xbdu\xfeZK\xc9\\m\xd3\x96\xe6\xe1O\xa1\x1a\xf6?FT\xbb\xc6\xee\x7f\x9d\xf5h\x1c\x0fq\xac\xb0y\x8dzOR\xcd\x08\n\xe6\x82Dx\xd3;\x9dj\x9a\x107\x1eS\r\xf9\x1f#\xaaAb\xb26\xa2\x01\xa8vS\x7f\xafp<6;\xd4{\x9aj\xe0\xf0"\x8btB\xd54^\xee\xa8jFj7\xfe\xc7\x88j\xb2O\xf6\x19g<v\x1b9%iLW\x8d\xef\x11.r0N\xa8\xdap\xean\\5\x1e\x15B\x9f1\xd5\xbe\xe1\x14\xda[\xe1z\xcc`O\xba>0\xa1\xd3U\xe3{\x04\x8a5O\xa7Z0x\xec$\xb22\xc8\x84\xf7\xa9f\xe4Lt\x9e\x0b\x1eS\rb\xcdGh@\xd6\xa3v<\xc0\x84~\xc5\x9d\x99j\x13S<\xa9\x8b}\xed\xd3\xa9f\x14\x92\x8f\x8f\x99\xa2Z\xe3\x7f\x8c\xa9\x06NY}N\x0cY\x8f\xcf\xf0l\xa1g\x93E\xaa\x9f\xe9\xbaS\x0f\x80+\x17\xa5\x00O\xa8Z\xe8\xba\x03\xa9\x81I\xaa\x19[\xb6H\xb6\xa3\xaaA\x0em\x0f\x01@>C\x19\x0f\xb1vq<\xf5\x94\xb9\xc6\xc6\x88\x02.\xebt\xaay\x83\'9\x07\xaa\xf5Gv\x05[%\xde\\Q\xcdU\xfb\xe2\xc3;\x91\xf5h\x1c\x8fK\xa9\xc4C0}_3\x02\x0b\xb9l\xd1\xe9TK\xa3\xa1%\xaa\xa8\xe69\xfd\xcbfm\xb2\xadq\xeb\x8e\xa8v\x85\x8chz\xd39\x1e\xc1R*\xf1\x10<A5\xc3B\x83?\xa1j|\x89\xf6\x8fq\xa2j\xc6\\\xa4 FT{\x8f#\x00a\x0c`\xbd\x83\t\xfd&\xf5\xd5\xa8\xa6\x06\x98k|\x0e{J\xd5Xt\xd0_*\xc4\x0b\xaa\x90S\xe29C\x9bM\xc9\r\xe9\x88j\xbf/Q9\x16\xcfz\xd4\x8e\x870\x13R<\xa5S-P\x1f+m\x1b\xa7T\xcd\xf0\xed\xdeo\xcb\xd8\xca\x93\xe6\x9a=\xb8l<gT\xb5klD-\xb6Dg\xe0\xef\x884os|U\x93\x1c\xaa\xb6\xaa\x07\xe2*\x9f\x87\x16\x1a\xf9\xe0^s\x14B\xe6\xe2\xab\xb2\x05\xa1\xcf\xe7\xda4\xd5\x98\x93.\xfdN\xa6\x9a:/wKT\x8e\xc5\xb3\x1eu\xc6\xe3\x91\xaf\xdc\xbddB\x99j\xa6\x9a\xbcn\x9e\xae\x14W\xe5R\xb1\xcciU3\xb6\xea"\r\xbcb\xceK\x99\xf0\x1c\xac\\\xcd\x99l\x88%\rzT3\xee\x91\x11\xf5f\xad\xe3\x01\xb1\xbb\xdc\xb50\x15\xd5\xe6E\xe3\xf4,,<\xce,\xc2[\xadr~{|<\xcbv\xbaB\xd6y%\x8a\xe9\n\xa9\x94i\xcdZ\xc3o20\x91jJi* N\xf7\xea\xa5\xc8\\\x8f\x9bOp\xdf\xf2 \x9e\xe2\t\x05s\xe1\xfbI\x92T\xbe_%\xdbp\xe1\xb4\xeb0t\x9d\xaa\te\xd2$\x92\xf6\x81\xd2\xeeyYG%\xf5M+r\x12/\xcb\xbc\xc4\xdd\nu\xbc\xc8\xb2\xac(\x03{\x10d\x96kr\xbfl\xf0\x01\x9dj\xf1\x82\xdd\x19\xa9\x1b\xdb\x07t\x12\xb5\xbei\x1c\x0f\x91\xfeF%\x1e\x06\x9f@\xfcv\x8c\xd5\xf9\xd7\x95\xcd.-*\xcf\xf3\xfc\xe2S\x81g\xd6\x1a\xc6\x9b\x9c\xce\x1e\x08\xe2<\ty=z3\xa1\xd2\xc0\x08\xd24\x867\x1b\xac\x85z\xc1\xf0\xb1O\x1b\xcc\x06\xf1*e\x94\xca\xf0\xbf\xe0\x94\xed\xf7\x8b\xda\xf1\x10\xa7W\xa8\xc4\x831O\x8d\xa0&\xad\x91*\xe4\xe7e\xce\xe7\xa1\x9f\xc9\xe1s\x19\xb3\x01\xf3\xf4\xf7\xf4_\xfc\x13 \x19\xd1\xb7\x173\x98\'"vG%\x1e\x84\xcc\xc3\x06\x95cE7u\xc6C\x1c(\xc8\xf1\x14\x81\x111U}\x92\xbc\x9d]\xa0\x0f\xef\xff\xc5Q\xfd\xd7\x11\x9eY]\xb2\x9c\xcf\xbe\xc3\x87\xf7(b z\x10Q@\x9dH\x8bg\x7f\x8b\xff\xee\xd4\x12\x0fBA\x98\xcb\xa6\x1ck\x06\x8e\x8a0\x11\xb8\xc4\x83P\x10\x89\xc9\xa6f\xb9v<\x84;"\xa7$\t\x99\r*\xc7z\x01\x81\x910\xa1\xcb\xe3\xd5\xfe\xfc\x1fp\x87\x8ch\x04.*?wW\xe2)BF$&k\x8f6\x01w\xff\xfe\\)\xf1 TD\x1cP\' \xeb\xb8g\x7f\x98\x92$d\x84\xc1\x94N>\x85\x81\x90J<\x08\x95\xddAVHT\x7fo(\x9e\xd2r\xa7f \xc5a\xc2\xf2_\x1b\xcf\xcf\x01\x1c\x18\xa3RR\x1ed\xa1\x7fuF\xf4!\x12\x93x\x1b\xe3\xf9]\x8a\xa7F\xb8U\xe2\xa7\xe0\x9e\xe2\xa9q\x84\xc9D\xe9nQ\xbaF\xf1\xd4\x18{\xf9\x9c\x1d\\\x91\x07\xcd\r\x84\x01F\x14\xd5tp\xb7\x97\xe2\xa9QD\xb9\xf7\xbe\x9d\\\xdc:4\xa9#b\x90wrb\x88\xff{x\x8a\xa7F\x81s\xbc\xb6.rsX\xe2A\x1c\xb2[\xe2h]\x9cZ\xed\xc9\x84\x8e\x11H\x87+\xc2\x84n\xb47\x10\x9cW\xf8 \x8f;\xbddB\'\x00\x7f\x1e\xeb\n\xb8;(\xf1 z\x81\xbf\xecq\x0e\x9c\x9d\xa9%\xf3D/\xf0\xaf\xd0\x10T\xe21\x81\x07U5*\xf1\x98\x82HLv(%\xf3D?\x8f\x8ajT\xe21\x05\xf8\xf3X\xdd\x02\xa5\x94\xe4\x14n\xe5\x8d\xad\xfb\xab\x88\x84\x867\x8aj\x14OMb)\xa9F\xe7S\xd3\x90\x8c(\xc5S\x13y\xdc,;\xf6T\xe21\x8d\xeb\x97\x18\x8a\x0c\x08\x82 \x08\x82 \x08\x82 \x08\x82 \x08\x82 \x08\x82 \x08\x82 \x08\x82 \x08\x82 \x08\x82 \x08\x82 \x08\x82 \x08\xc2\xf8\x1f\xa8\xf8\xbd\xf8\x98\x8d^\x19\x00\x00\x00\x00IEND\xaeB`\x82')
            )

cur.execute("INSERT INTO posts (nome, tipo, estado, cidade, rua, numero, telefone, email, redes, conteudo, username, password, foto) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ? , ?, ?, ?, ?)",
            ('ONG exemplo y', 'ONG de crianças', 'SP', 'São Paulo', 'Avenida Rebouças', '900 - Bloco A', '119454325465', 'ongcrianca@hotmail.com', '@ONG de criança', 'Para ajudar a instituição, entre em contato pelo email casadoscurumins.br@gmail.com ou pelo telefone 11-56725131, e marque uma vista com o responsável. Todas as instituições gostam de ser visitadas, desde que se tenha o cuidado de marcar antes a visita.', 'username1', 'password1',
            b'\x89PNG\r\n\x1a\n\x00\x00\x00\rIHDR\x00\x00\x015\x00\x00\x00\xa3\x08\x03\x00\x00\x00\xdc\x89y\xdc\x00\x00\x00\xc3PLTE\xff\xff\xff\xd129\x1d\x1d\x1b\x87\x87\x87}}}\x82\x82\x82\x80\x80\x80\x00\x00\x00\x84\x84\x84\xbc\xbc\xbc\xb4\xb4\xb4\xe6\xe6\xe6\xf4\xf4\xf4\x99\x99\x99\x8a\x8a\x8a|||\xcf"+\xde\xde\xde\xa4\xa4\xa4\xec\xec\xec\xcb\xcb\xcb\xc5\xc5\xc5\xe2\xe2\xe2\x91\x91\x91\xd0-4\xd2\xd2\xd2IIH\x16\x16\x13\xf2\xf2\xf2\xe8\xaa\xac\xd0(0\xcf\x1c&\xd8W\\\xa1\xa1\xa1\xd5OT\xac\xac\xac\xf0\xc7\xc9\xf3\xd3\xd4\xfa\xeb\xec\x0b\x0b\x07\xf6\xdb\xdc\xee\xbd\xbf^^]\xe7\xa0\xa3\xe0\x86\x89\xe3\x8f\x92\xd4DJ>>=\xde{~nnm$$"\xce\x0e\x1b\xd29@\xda`e\xfc\xf0\xf0\xe9\xa5\xa7\xec\xb6\xb8--,\xe2\x8c\x8f\xee\xc1\xc3\xd8\\a\xdbim997ffe\xdborv9\xe8\xfd\x00\x00\n`IDATx\x9c\xed\x9c{\x7f\x9b6\x17\xc7\xc9\xb8\x180\x18s3\xa1q\xe3:4N\xd3K\xba\xd6Y\xd6uk\x97\xf7\xff\xaa\x1eI\x87\xcb\x91\x0c\x82,\xb5\xb7>\x9f\xf3\xfdg\x93\x11X\xfe!\xe9\\t\x1a\xc3 \x08\x82 \x08\x82 \x08\x82 \x08\x82 \x08\x82 \x08\x82 \x08\x82 \x08\x82 \x08\x82 \x08\x82 \x08\x82 \x08\x82 \x88\xff<\x99\xefey^\xc5=\x97V\xdb\xa4b$\xb9h\xa5\xc9\x96\xfd\x7fh\x06\xfd\x8f\xc9\xcb\xb2\xcc=O4\xca,f\xb0f\n\x17__\xbdb\\\xddB+\xf9\xf8\x02\xf1\x1d\x9e\xf7\x06\xba|\x81\xfb\xc30,\x16\x02\x97\x93\x1f~\xdf\xdcK\xc20\xf1\xca5\xfa,\xf0}\xcf\xaf\xb6!\xbb\xc9,\xaa<}\xb2\x16O \x8bl\xdb\xaaz/\x05|\xd0V;\xe6\xd2a\xcd\xb0\xff)\x81\x179\x8e\xd3h_\xf2F\xe47\x17w\xfbs\xc6\xe6\x1d\xb4\xaa\xd9E\xc7\xcdg\xf8\xf0\xb5\xe8\xb2\xbf\x86Vn\xb1\x1f\x1e&I\xe2s!\x8aH\xfd\xb6y\x11UY\x99ya\x14\x15U\'\xdc\xca\xb1]{\x9b\xc7\xf3\xf9<c\x97\xc2r\xb2\x08O\xc7sM{\xde\x7f)vL\xb3\xe8\x9a\x99m\x9a\x8b\xa1\xc7$\xae\x9d\xe3\x9eX\xdf\xcb3\xc6\xf9o\xd0(g\xbft\\\xbc\x85\x0f\xdf-y\x97\xcb]}\x83)\xdd\xee+\xc3\xcb\xa3\xe6\x9b\xd2\xd0\xb6\x906\xeck\xdb77/\x86&\xc3\x0fa\xc5\xa4\xe9_vF\xc0~\xbc/\xf7t\xb2\x81\xc7\x94\x8e\xd3\xfd\xb8\xb5e\xba^w\xed\xafs\xae\xda\x1d4R\xac\xdaM=\x8f~\xbdD=\xf8+\x90&5^\x87\\4\xa4b\x12\xe1\x01E\x9djF\x10\xbav20\xd8\xe7\x93Z\xc3\xaa\x99&\x9a@B5\xd3\xea\xdb\x02\xc5E\x1b=\xc52m\xa4\xda{1\xd9\xce\x1e\xe0\xa1\x7f\\t\xaa\xcd\xb6\xd0\xe37\xa1\xeb\xb7\xe6\x06\x7fp+`\x93\xe8\x93\xb4\xf2\n\xac\xda\x02\xa9\xc6G\xef\xf4l\x89?\x86\xb5F5GV\xcd*\x16L\xc7\xfem6\xb5\xdcA\xd5^\x8a\xf5\xb7y\x03\xad\x17X\xb5\xfa\xf1\xb0@?47\xe8T\x0b\x0b\xa99\xc7\x1aJ\xaa\x19\xb9m\xda\x03\xbf\xec\xd9\x04\xee\xb0j\x96\xacZT\xad"\xd3]\xf4\xf6\xd6\xa9v\xbd\x11\xaa\xfd\t\xadO7H5\xf8\x91\x0f{\xd1\xe1\xb6\xb9A\xa3Z\x1ay\x03W\x0c\xa1\xda\n5]i\xf8?\x94\x11\xd5\xd0\xab\\E\x89\x919\xa6[\xf4\xf5\xd5\xa9\xb6\xbb\xc4S\xa9@\x1b\xdb\x0c\xeey\xbd\xc1\x93Q\xabZ\x16\r\xed\xac\x86P\r[\x8eJ3e\x9f\xc9\xd3T3|\xb6j\xfb6Y\x9dj\x86\xd8\xd6.\x7f\x85\x86\x87\xcd\x01|T/\xe1\xb6\xbfF5\xdf\xd2L\x1fE5fS\x07m\xfe3a\xaa\xb9OP\xcdH\x98y\xf7\x0f\xfb2\xa32\xac\x1al\xf6\xf7\xd0@\xae\xc7\xc5\x0b\xf8\xe8\x830\xa1\xaf\xda\xfe\x1a\xd5\xaa\xbe/oPT\x8b\x87\xdd\x83\xe7\xc2T\x1bz!\x8aj\xb1%&Y\xe8\xf6\xf9\x1f\xa9\x85\x9f\xa2\xa8&T9\xdbCc\xdd\xa9v\xe3\xc0G\xaf\xb8\xaa\x97\xef\xdb\xfe:\xd5\xec\xde\r\x02PT\xd3\xb8\x07\xcfe\xbaj%\xa8\xc6B\x86\x1e\xffC\xab\xda\x17\xb1\x02\xf7\xb5\x13\xdb\xa96\xab\xd7\xfa\x1dWm\xf9{\xdb_\xa3\x9ag;\xc3>\xbf\xa2\xda\xdc9\xe6\n}\x9ajF\xca&\xfeA8\xa1U\xed\x8ddD?\xb6\xaeG\xedx\xec\xce\xc5\xe5\xeb\xb6\xbfF5\xb6\xea\xdc\xc1\x10\xf3`\x85\xba\xdb\xa1\xae\xcfd=\xfcB\x98jN\x8fj\xec\x7fLW\x9d\xfaZ\xd5\x1e\xc4\n]\xbe\x84V\xd4\xba\x1e3\xf8\x8d \xear\xd7\xf6\xd7\xf9k\x0b\xd3u\xd7\x83\xd7$\xd5r\xfbh\x9e\x07\xf3r\x87Tc\xfb\x02\xf6\x7fZ\xd5Xx}\xe0\x7fhU\xab7\xaeGh\x84\xed\x12\xbd\x80\x9f\x7f+T;\xeb\xba\xebT\x8b\xd9w\xbb\xab\xfek\x8aj,\xa6:\x96\x97\xabQ\x8d\xed\x0b\xb2jm8\\\xd9\xaa\xff\xa1W\r\xe2\xcc\xbf\xa0\xe17\xaa]|\x84\x0f>\xe0\xab\xa2\x87+\xbd\x14yE\xb2\xef6\xdd\xfe\xb8\xce\x94T[;\xb6\xc6\xde>\x8f\'\xa8\xd6%\x7f\x84!\x95\x86\xa4W\rr\x1a\xf7\x10\x89\xc6\xadju\xc6Ch\xda\xc5S\\5\x9ck\x89\x95\xdf\xce|\x1f\xd3\xea\x8d\x10B\x17\xab\x968\x1as\xfbLV\xc3\xfb\x9aF5nH\xa5\xd8X\xaf\x1a8\xff\xb5\x11\x9d7\xfbZ\xe3x\x80\t\xfd\xd2u\xe7\xaa\x05\x8c4M\xe3\xf2\xd0\xafM\xb89\n{\x16\x9f\xa4Z\x16\x15\xc7Z\x9f\xffT5aHq\xa8\xacWm\xb7\xc7V\xb2\xc9z\xcc\xea\x15\xbf\x97\xe3)\xa1\x9a\x19\xd5X=[\xba\xc7\x1c1\xd7=\xf4@\x90jA\xf5\xe9\x88\xe9\xb5\x7f\xaa\x9ap\xbc\x9dn\xc7\x89\xb5\xaa\x19`%k\x8f\xac\xc9z4\x8e\x87P\xed\xf2\xa1\xeb\xcdUK*/gx~\xd8\x13C\xc5.\xeba\x1d\xecZB\xb5<+\xcb|\xbb\xf0\x8f\x9a\x02\x1fQ\r\xed\x13\xa5<LnH\xbb\xfc\xc7\x88jW\xc2\x88~\x85F\x93\xf5\x98\xc1+\xf9\x93Kz~\x85z\xcb64\xed\x89\xd7\xd7a\xdf*\x15\xaa\xad\xe7q<\x1f\xf2M~\x14z\xd5p6-S^\xae\x8f\xf3\x1fL\xb5\xe18\xd40\xbe^"e\xb6\xb59\x98AS\xc4\xeeMl\x0fO\x96=\x8f\xde\xedI\xacR[\xb6\xa5\x8a\xe7qDFTC\xa3PU\xe3\xc6\xac\xf5?b\x0b\x1b\xac\x03\xd5 \xab\xb1\x84F\x93\xf5\xa8\x8fZ\x84\t]\xbeC\xbdu\xfeZK\xc9\\m\xd3\x96\xe6\xe1O\xa1\x1a\xf6?FT\xbb\xc6\xee\x7f\x9d\xf5h\x1c\x0fq\xac\xb0y\x8dzOR\xcd\x08\n\xe6\x82Dx\xd3;\x9dj\x9a\x107\x1eS\r\xf9\x1f#\xaaAb\xb26\xa2\x01\xa8vS\x7f\xafp<6;\xd4{\x9aj\xe0\xf0"\x8btB\xd54^\xee\xa8jFj7\xfe\xc7\x88j\xb2O\xf6\x19g<v\x1b9%iLW\x8d\xef\x11.r0N\xa8\xdap\xean\\5\x1e\x15B\x9f1\xd5\xbe\xe1\x14\xda[\xe1z\xcc`O\xba>0\xa1\xd3U\xe3{\x04\x8a5O\xa7Z0x\xec$\xb22\xc8\x84\xf7\xa9f\xe4Lt\x9e\x0b\x1eS\rb\xcdGh@\xd6\xa3v<\xc0\x84~\xc5\x9d\x99j\x13S<\xa9\x8b}\xed\xd3\xa9f\x14\x92\x8f\x8f\x99\xa2Z\xe3\x7f\x8c\xa9\x06NY}N\x0cY\x8f\xcf\xf0l\xa1g\x93E\xaa\x9f\xe9\xbaS\x0f\x80+\x17\xa5\x00O\xa8Z\xe8\xba\x03\xa9\x81I\xaa\x19[\xb6H\xb6\xa3\xaaA\x0em\x0f\x01@>C\x19\x0f\xb1vq<\xf5\x94\xb9\xc6\xc6\x88\x02.\xebt\xaay\x83\'9\x07\xaa\xf5Gv\x05[%\xde\\Q\xcdU\xfb\xe2\xc3;\x91\xf5h\x1c\x8fK\xa9\xc4C0}_3\x02\x0b\xb9l\xd1\xe9TK\xa3\xa1%\xaa\xa8\xe69\xfd\xcbfm\xb2\xadq\xeb\x8e\xa8v\x85\x8chz\xd39\x1e\xc1R*\xf1\x10<A5\xc3B\x83?\xa1j|\x89\xf6\x8fq\xa2j\xc6\\\xa4 FT{\x8f#\x00a\x0c`\xbd\x83\t\xfd&\xf5\xd5\xa8\xa6\x06\x98k|\x0e{J\xd5Xt\xd0_*\xc4\x0b\xaa\x90S\xe29C\x9bM\xc9\r\xe9\x88j\xbf/Q9\x16\xcfz\xd4\x8e\x870\x13R<\xa5S-P\x1f+m\x1b\xa7T\xcd\xf0\xed\xdeo\xcb\xd8\xca\x93\xe6\x9a=\xb8l<gT\xb5klD-\xb6Dg\xe0\xef\x884os|U\x93\x1c\xaa\xb6\xaa\x07\xe2*\x9f\x87\x16\x1a\xf9\xe0^s\x14B\xe6\xe2\xab\xb2\x05\xa1\xcf\xe7\xda4\xd5\x98\x93.\xfdN\xa6\x9a:/wKT\x8e\xc5\xb3\x1eu\xc6\xe3\x91\xaf\xdc\xbddB\x99j\xa6\x9a\xbcn\x9e\xae\x14W\xe5R\xb1\xcciU3\xb6\xea"\r\xbcb\xceK\x99\xf0\x1c\xac\\\xcd\x99l\x88%\rzT3\xee\x91\x11\xf5f\xad\xe3\x01\xb1\xbb\xdc\xb50\x15\xd5\xe6E\xe3\xf4,,<\xce,\xc2[\xadr~{|<\xcbv\xbaB\xd6y%\x8a\xe9\n\xa9\x94i\xcdZ\xc3o20\x91jJi* N\xf7\xea\xa5\xc8\\\x8f\x9bOp\xdf\xf2 \x9e\xe2\t\x05s\xe1\xfbI\x92T\xbe_%\xdbp\xe1\xb4\xeb0t\x9d\xaa\te\xd2$\x92\xf6\x81\xd2\xeeyYG%\xf5M+r\x12/\xcb\xbc\xc4\xdd\nu\xbc\xc8\xb2\xac(\x03{\x10d\x96kr\xbfl\xf0\x01\x9dj\xf1\x82\xdd\x19\xa9\x1b\xdb\x07t\x12\xb5\xbei\x1c\x0f\x91\xfeF%\x1e\x06\x9f@\xfcv\x8c\xd5\xf9\xd7\x95\xcd.-*\xcf\xf3\xfc\xe2S\x81g\xd6\x1a\xc6\x9b\x9c\xce\x1e\x08\xe2<\ty=z3\xa1\xd2\xc0\x08\xd24\x867\x1b\xac\x85z\xc1\xf0\xb1O\x1b\xcc\x06\xf1*e\x94\xca\xf0\xbf\xe0\x94\xed\xf7\x8b\xda\xf1\x10\xa7W\xa8\xc4\x831O\x8d\xa0&\xad\x91*\xe4\xe7e\xce\xe7\xa1\x9f\xc9\xe1s\x19\xb3\x01\xf3\xf4\xf7\xf4_\xfc\x13 \x19\xd1\xb7\x173\x98\'"vG%\x1e\x84\xcc\xc3\x06\x95cE7u\xc6C\x1c(\xc8\xf1\x14\x81\x111U}\x92\xbc\x9d]\xa0\x0f\xef\xff\xc5Q\xfd\xd7\x11\x9eY]\xb2\x9c\xcf\xbe\xc3\x87\xf7(b z\x10Q@\x9dH\x8bg\x7f\x8b\xff\xee\xd4\x12\x0fBA\x98\xcb\xa6\x1ck\x06\x8e\x8a0\x11\xb8\xc4\x83P\x10\x89\xc9\xa6f\xb9v<\x84;"\xa7$\t\x99\r*\xc7z\x01\x81\x910\xa1\xcb\xe3\xd5\xfe\xfc\x1fp\x87\x8ch\x04.*?wW\xe2)BF$&k\x8f6\x01w\xff\xfe\\)\xf1 TD\x1cP\' \xeb\xb8g\x7f\x98\x92$d\x84\xc1\x94N>\x85\x81\x90J<\x08\x95\xddAVHT\x7fo(\x9e\xd2r\xa7f \xc5a\xc2\xf2_\x1b\xcf\xcf\x01\x1c\x18\xa3RR\x1ed\xa1\x7fuF\xf4!\x12\x93x\x1b\xe3\xf9]\x8a\xa7F\xb8U\xe2\xa7\xe0\x9e\xe2\xa9q\x84\xc9D\xe9nQ\xbaF\xf1\xd4\x18{\xf9\x9c\x1d\\\x91\x07\xcd\r\x84\x01F\x14\xd5tp\xb7\x97\xe2\xa9QD\xb9\xf7\xbe\x9d\\\xdc:4\xa9#b\x90wrb\x88\xff{x\x8a\xa7F\x81s\xbc\xb6.rsX\xe2A\x1c\xb2[\xe2h]\x9cZ\xed\xc9\x84\x8e\x11H\x87+\xc2\x84n\xb47\x10\x9cW\xf8 \x8f;\xbddB\'\x00\x7f\x1e\xeb\n\xb8;(\xf1 z\x81\xbf\xecq\x0e\x9c\x9d\xa9%\xf3D/\xf0\xaf\xd0\x10T\xe21\x81\x07U5*\xf1\x98\x82HLv(%\xf3D?\x8f\x8ajT\xe21\x05\xf8\xf3X\xdd\x02\xa5\x94\xe4\x14n\xe5\x8d\xad\xfb\xab\x88\x84\x867\x8aj\x14OMb)\xa9F\xe7S\xd3\x90\x8c(\xc5S\x13y\xdc,;\xf6T\xe21\x8d\xeb\x97\x18\x8a\x0c\x08\x82 \x08\x82 \x08\x82 \x08\x82 \x08\x82 \x08\x82 \x08\x82 \x08\x82 \x08\x82 \x08\x82 \x08\x82 \x08\x82 \x08\xc2\xf8\x1f\xa8\xf8\xbd\xf8\x98\x8d^\x19\x00\x00\x00\x00IEND\xaeB`\x82')
            )

cur.execute("INSERT INTO posts (nome, tipo, estado, cidade, rua, numero, telefone, email, redes, conteudo, username, password, foto) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ? , ?, ?, ?, ?)",
            ('ONG exemplo z', 'ONG de crianças', 'SP', 'São Paulo', 'Avenida Rebouças', '900 - Bloco A', '119454325465', 'ongcrianca@hotmail.com', '@ONG de criança', 'Para ajudar a instituição, entre em contato pelo email casadoscurumins.br@gmail.com ou pelo telefone 11-56725131, e marque uma vista com o responsável. Todas as instituições gostam de ser visitadas, desde que se tenha o cuidado de marcar antes a visita.', 'username1', 'password1',
            b'\x89PNG\r\n\x1a\n\x00\x00\x00\rIHDR\x00\x00\x015\x00\x00\x00\xa3\x08\x03\x00\x00\x00\xdc\x89y\xdc\x00\x00\x00\xc3PLTE\xff\xff\xff\xd129\x1d\x1d\x1b\x87\x87\x87}}}\x82\x82\x82\x80\x80\x80\x00\x00\x00\x84\x84\x84\xbc\xbc\xbc\xb4\xb4\xb4\xe6\xe6\xe6\xf4\xf4\xf4\x99\x99\x99\x8a\x8a\x8a|||\xcf"+\xde\xde\xde\xa4\xa4\xa4\xec\xec\xec\xcb\xcb\xcb\xc5\xc5\xc5\xe2\xe2\xe2\x91\x91\x91\xd0-4\xd2\xd2\xd2IIH\x16\x16\x13\xf2\xf2\xf2\xe8\xaa\xac\xd0(0\xcf\x1c&\xd8W\\\xa1\xa1\xa1\xd5OT\xac\xac\xac\xf0\xc7\xc9\xf3\xd3\xd4\xfa\xeb\xec\x0b\x0b\x07\xf6\xdb\xdc\xee\xbd\xbf^^]\xe7\xa0\xa3\xe0\x86\x89\xe3\x8f\x92\xd4DJ>>=\xde{~nnm$$"\xce\x0e\x1b\xd29@\xda`e\xfc\xf0\xf0\xe9\xa5\xa7\xec\xb6\xb8--,\xe2\x8c\x8f\xee\xc1\xc3\xd8\\a\xdbim997ffe\xdborv9\xe8\xfd\x00\x00\n`IDATx\x9c\xed\x9c{\x7f\x9b6\x17\xc7\xc9\xb8\x180\x18s3\xa1q\xe3:4N\xd3K\xba\xd6Y\xd6uk\x97\xf7\xff\xaa\x1eI\x87\xcb\x91\x0c\x82,\xb5\xb7>\x9f\xf3\xfdg\x93\x11X\xfe!\xe9\\t\x1a\xc3 \x08\x82 \x08\x82 \x08\x82 \x08\x82 \x08\x82 \x08\x82 \x08\x82 \x08\x82 \x08\x82 \x08\x82 \x08\x82 \x08\x82 \x88\xff<\x99\xefey^\xc5=\x97V\xdb\xa4b$\xb9h\xa5\xc9\x96\xfd\x7fh\x06\xfd\x8f\xc9\xcb\xb2\xcc=O4\xca,f\xb0f\n\x17__\xbdb\\\xddB+\xf9\xf8\x02\xf1\x1d\x9e\xf7\x06\xba|\x81\xfb\xc30,\x16\x02\x97\x93\x1f~\xdf\xdcK\xc20\xf1\xca5\xfa,\xf0}\xcf\xaf\xb6!\xbb\xc9,\xaa<}\xb2\x16O \x8bl\xdb\xaaz/\x05|\xd0V;\xe6\xd2a\xcd\xb0\xff)\x81\x179\x8e\xd3h_\xf2F\xe47\x17w\xfbs\xc6\xe6\x1d\xb4\xaa\xd9E\xc7\xcdg\xf8\xf0\xb5\xe8\xb2\xbf\x86Vn\xb1\x1f\x1e&I\xe2s!\x8aH\xfd\xb6y\x11UY\x99ya\x14\x15U\'\xdc\xca\xb1]{\x9b\xc7\xf3\xf9<c\x97\xc2r\xb2\x08O\xc7sM{\xde\x7f)vL\xb3\xe8\x9a\x99m\x9a\x8b\xa1\xc7$\xae\x9d\xe3\x9eX\xdf\xcb3\xc6\xf9o\xd0(g\xbft\\\xbc\x85\x0f\xdf-y\x97\xcb]}\x83)\xdd\xee+\xc3\xcb\xa3\xe6\x9b\xd2\xd0\xb6\x906\xeck\xdb77/\x86&\xc3\x0fa\xc5\xa4\xe9_vF\xc0~\xbc/\xf7t\xb2\x81\xc7\x94\x8e\xd3\xfd\xb8\xb5e\xba^w\xed\xafs\xae\xda\x1d4R\xac\xdaM=\x8f~\xbdD=\xf8+\x90&5^\x87\\4\xa4b\x12\xe1\x01E\x9djF\x10\xbav20\xd8\xe7\x93Z\xc3\xaa\x99&\x9a@B5\xd3\xea\xdb\x02\xc5E\x1b=\xc52m\xa4\xda{1\xd9\xce\x1e\xe0\xa1\x7f\\t\xaa\xcd\xb6\xd0\xe37\xa1\xeb\xb7\xe6\x06\x7fp+`\x93\xe8\x93\xb4\xf2\n\xac\xda\x02\xa9\xc6G\xef\xf4l\x89?\x86\xb5F5GV\xcd*\x16L\xc7\xfem6\xb5\xdcA\xd5^\x8a\xf5\xb7y\x03\xad\x17X\xb5\xfa\xf1\xb0@?47\xe8T\x0b\x0b\xa99\xc7\x1aJ\xaa\x19\xb9m\xda\x03\xbf\xec\xd9\x04\xee\xb0j\x96\xacZT\xad"\xd3]\xf4\xf6\xd6\xa9v\xbd\x11\xaa\xfd\t\xadO7H5\xf8\x91\x0f{\xd1\xe1\xb6\xb9A\xa3Z\x1ay\x03W\x0c\xa1\xda\n5]i\xf8?\x94\x11\xd5\xd0\xab\\E\x89\x919\xa6[\xf4\xf5\xd5\xa9\xb6\xbb\xc4S\xa9@\x1b\xdb\x0c\xeey\xbd\xc1\x93Q\xabZ\x16\r\xed\xac\x86P\r[\x8eJ3e\x9f\xc9\xd3T3|\xb6j\xfb6Y\x9dj\x86\xd8\xd6.\x7f\x85\x86\x87\xcd\x01|T/\xe1\xb6\xbfF5\xdf\xd2L\x1fE5fS\x07m\xfe3a\xaa\xb9OP\xcdH\x98y\xf7\x0f\xfb2\xa32\xac\x1al\xf6\xf7\xd0@\xae\xc7\xc5\x0b\xf8\xe8\x830\xa1\xaf\xda\xfe\x1a\xd5\xaa\xbe/oPT\x8b\x87\xdd\x83\xe7\xc2T\x1bz!\x8aj\xb1%&Y\xe8\xf6\xf9\x1f\xa9\x85\x9f\xa2\xa8&T9\xdbCc\xdd\xa9v\xe3\xc0G\xaf\xb8\xaa\x97\xef\xdb\xfe:\xd5\xec\xde\r\x02PT\xd3\xb8\x07\xcfe\xbaj%\xa8\xc6B\x86\x1e\xffC\xab\xda\x17\xb1\x02\xf7\xb5\x13\xdb\xa96\xab\xd7\xfa\x1dWm\xf9{\xdb_\xa3\x9ag;\xc3>\xbf\xa2\xda\xdc9\xe6\n}\x9ajF\xca&\xfeA8\xa1U\xed\x8ddD?\xb6\xaeG\xedx\xec\xce\xc5\xe5\xeb\xb6\xbfF5\xb6\xea\xdc\xc1\x10\xf3`\x85\xba\xdb\xa1\xae\xcfd=\xfcB\x98jN\x8fj\xec\x7fLW\x9d\xfaZ\xd5\x1e\xc4\n]\xbe\x84V\xd4\xba\x1e3\xf8\x8d \xear\xd7\xf6\xd7\xf9k\x0b\xd3u\xd7\x83\xd7$\xd5r\xfbh\x9e\x07\xf3r\x87Tc\xfb\x02\xf6\x7fZ\xd5Xx}\xe0\x7fhU\xab7\xaeGh\x84\xed\x12\xbd\x80\x9f\x7f+T;\xeb\xba\xebT\x8b\xd9w\xbb\xab\xfek\x8aj,\xa6:\x96\x97\xabQ\x8d\xed\x0b\xb2jm8\\\xd9\xaa\xff\xa1W\r\xe2\xcc\xbf\xa0\xe17\xaa]|\x84\x0f>\xe0\xab\xa2\x87+\xbd\x14yE\xb2\xef6\xdd\xfe\xb8\xce\x94T[;\xb6\xc6\xde>\x8f\'\xa8\xd6%\x7f\x84!\x95\x86\xa4W\rr\x1a\xf7\x10\x89\xc6\xadju\xc6Ch\xda\xc5S\\5\x9ck\x89\x95\xdf\xce|\x1f\xd3\xea\x8d\x10B\x17\xab\x968\x1as\xfbLV\xc3\xfb\x9aF5nH\xa5\xd8X\xaf\x1a8\xff\xb5\x11\x9d7\xfbZ\xe3x\x80\t\xfd\xd2u\xe7\xaa\x05\x8c4M\xe3\xf2\xd0\xafM\xb89\n{\x16\x9f\xa4Z\x16\x15\xc7Z\x9f\xffT5aHq\xa8\xacWm\xb7\xc7V\xb2\xc9z\xcc\xea\x15\xbf\x97\xe3)\xa1\x9a\x19\xd5X=[\xba\xc7\x1c1\xd7=\xf4@\x90jA\xf5\xe9\x88\xe9\xb5\x7f\xaa\x9ap\xbc\x9dn\xc7\x89\xb5\xaa\x19`%k\x8f\xac\xc9z4\x8e\x87P\xed\xf2\xa1\xeb\xcdUK*/gx~\xd8\x13C\xc5.\xeba\x1d\xecZB\xb5<+\xcb|\xbb\xf0\x8f\x9a\x02\x1fQ\r\xed\x13\xa5<LnH\xbb\xfc\xc7\x88jW\xc2\x88~\x85F\x93\xf5\x98\xc1+\xf9\x93Kz~\x85z\xcb64\xed\x89\xd7\xd7a\xdf*\x15\xaa\xad\xe7q<\x1f\xf2M~\x14z\xd5p6-S^\xae\x8f\xf3\x1fL\xb5\xe18\xd40\xbe^"e\xb6\xb59\x98AS\xc4\xeeMl\x0fO\x96=\x8f\xde\xedI\xacR[\xb6\xa5\x8a\xe7qDFTC\xa3PU\xe3\xc6\xac\xf5?b\x0b\x1b\xac\x03\xd5 \xab\xb1\x84F\x93\xf5\xa8\x8fZ\x84\t]\xbeC\xbdu\xfeZK\xc9\\m\xd3\x96\xe6\xe1O\xa1\x1a\xf6?FT\xbb\xc6\xee\x7f\x9d\xf5h\x1c\x0fq\xac\xb0y\x8dzOR\xcd\x08\n\xe6\x82Dx\xd3;\x9dj\x9a\x107\x1eS\r\xf9\x1f#\xaaAb\xb26\xa2\x01\xa8vS\x7f\xafp<6;\xd4{\x9aj\xe0\xf0"\x8btB\xd54^\xee\xa8jFj7\xfe\xc7\x88j\xb2O\xf6\x19g<v\x1b9%iLW\x8d\xef\x11.r0N\xa8\xdap\xean\\5\x1e\x15B\x9f1\xd5\xbe\xe1\x14\xda[\xe1z\xcc`O\xba>0\xa1\xd3U\xe3{\x04\x8a5O\xa7Z0x\xec$\xb22\xc8\x84\xf7\xa9f\xe4Lt\x9e\x0b\x1eS\rb\xcdGh@\xd6\xa3v<\xc0\x84~\xc5\x9d\x99j\x13S<\xa9\x8b}\xed\xd3\xa9f\x14\x92\x8f\x8f\x99\xa2Z\xe3\x7f\x8c\xa9\x06NY}N\x0cY\x8f\xcf\xf0l\xa1g\x93E\xaa\x9f\xe9\xbaS\x0f\x80+\x17\xa5\x00O\xa8Z\xe8\xba\x03\xa9\x81I\xaa\x19[\xb6H\xb6\xa3\xaaA\x0em\x0f\x01@>C\x19\x0f\xb1vq<\xf5\x94\xb9\xc6\xc6\x88\x02.\xebt\xaay\x83\'9\x07\xaa\xf5Gv\x05[%\xde\\Q\xcdU\xfb\xe2\xc3;\x91\xf5h\x1c\x8fK\xa9\xc4C0}_3\x02\x0b\xb9l\xd1\xe9TK\xa3\xa1%\xaa\xa8\xe69\xfd\xcbfm\xb2\xadq\xeb\x8e\xa8v\x85\x8chz\xd39\x1e\xc1R*\xf1\x10<A5\xc3B\x83?\xa1j|\x89\xf6\x8fq\xa2j\xc6\\\xa4 FT{\x8f#\x00a\x0c`\xbd\x83\t\xfd&\xf5\xd5\xa8\xa6\x06\x98k|\x0e{J\xd5Xt\xd0_*\xc4\x0b\xaa\x90S\xe29C\x9bM\xc9\r\xe9\x88j\xbf/Q9\x16\xcfz\xd4\x8e\x870\x13R<\xa5S-P\x1f+m\x1b\xa7T\xcd\xf0\xed\xdeo\xcb\xd8\xca\x93\xe6\x9a=\xb8l<gT\xb5klD-\xb6Dg\xe0\xef\x884os|U\x93\x1c\xaa\xb6\xaa\x07\xe2*\x9f\x87\x16\x1a\xf9\xe0^s\x14B\xe6\xe2\xab\xb2\x05\xa1\xcf\xe7\xda4\xd5\x98\x93.\xfdN\xa6\x9a:/wKT\x8e\xc5\xb3\x1eu\xc6\xe3\x91\xaf\xdc\xbddB\x99j\xa6\x9a\xbcn\x9e\xae\x14W\xe5R\xb1\xcciU3\xb6\xea"\r\xbcb\xceK\x99\xf0\x1c\xac\\\xcd\x99l\x88%\rzT3\xee\x91\x11\xf5f\xad\xe3\x01\xb1\xbb\xdc\xb50\x15\xd5\xe6E\xe3\xf4,,<\xce,\xc2[\xadr~{|<\xcbv\xbaB\xd6y%\x8a\xe9\n\xa9\x94i\xcdZ\xc3o20\x91jJi* N\xf7\xea\xa5\xc8\\\x8f\x9bOp\xdf\xf2 \x9e\xe2\t\x05s\xe1\xfbI\x92T\xbe_%\xdbp\xe1\xb4\xeb0t\x9d\xaa\te\xd2$\x92\xf6\x81\xd2\xeeyYG%\xf5M+r\x12/\xcb\xbc\xc4\xdd\nu\xbc\xc8\xb2\xac(\x03{\x10d\x96kr\xbfl\xf0\x01\x9dj\xf1\x82\xdd\x19\xa9\x1b\xdb\x07t\x12\xb5\xbei\x1c\x0f\x91\xfeF%\x1e\x06\x9f@\xfcv\x8c\xd5\xf9\xd7\x95\xcd.-*\xcf\xf3\xfc\xe2S\x81g\xd6\x1a\xc6\x9b\x9c\xce\x1e\x08\xe2<\ty=z3\xa1\xd2\xc0\x08\xd24\x867\x1b\xac\x85z\xc1\xf0\xb1O\x1b\xcc\x06\xf1*e\x94\xca\xf0\xbf\xe0\x94\xed\xf7\x8b\xda\xf1\x10\xa7W\xa8\xc4\x831O\x8d\xa0&\xad\x91*\xe4\xe7e\xce\xe7\xa1\x9f\xc9\xe1s\x19\xb3\x01\xf3\xf4\xf7\xf4_\xfc\x13 \x19\xd1\xb7\x173\x98\'"vG%\x1e\x84\xcc\xc3\x06\x95cE7u\xc6C\x1c(\xc8\xf1\x14\x81\x111U}\x92\xbc\x9d]\xa0\x0f\xef\xff\xc5Q\xfd\xd7\x11\x9eY]\xb2\x9c\xcf\xbe\xc3\x87\xf7(b z\x10Q@\x9dH\x8bg\x7f\x8b\xff\xee\xd4\x12\x0fBA\x98\xcb\xa6\x1ck\x06\x8e\x8a0\x11\xb8\xc4\x83P\x10\x89\xc9\xa6f\xb9v<\x84;"\xa7$\t\x99\r*\xc7z\x01\x81\x910\xa1\xcb\xe3\xd5\xfe\xfc\x1fp\x87\x8ch\x04.*?wW\xe2)BF$&k\x8f6\x01w\xff\xfe\\)\xf1 TD\x1cP\' \xeb\xb8g\x7f\x98\x92$d\x84\xc1\x94N>\x85\x81\x90J<\x08\x95\xddAVHT\x7fo(\x9e\xd2r\xa7f \xc5a\xc2\xf2_\x1b\xcf\xcf\x01\x1c\x18\xa3RR\x1ed\xa1\x7fuF\xf4!\x12\x93x\x1b\xe3\xf9]\x8a\xa7F\xb8U\xe2\xa7\xe0\x9e\xe2\xa9q\x84\xc9D\xe9nQ\xbaF\xf1\xd4\x18{\xf9\x9c\x1d\\\x91\x07\xcd\r\x84\x01F\x14\xd5tp\xb7\x97\xe2\xa9QD\xb9\xf7\xbe\x9d\\\xdc:4\xa9#b\x90wrb\x88\xff{x\x8a\xa7F\x81s\xbc\xb6.rsX\xe2A\x1c\xb2[\xe2h]\x9cZ\xed\xc9\x84\x8e\x11H\x87+\xc2\x84n\xb47\x10\x9cW\xf8 \x8f;\xbddB\'\x00\x7f\x1e\xeb\n\xb8;(\xf1 z\x81\xbf\xecq\x0e\x9c\x9d\xa9%\xf3D/\xf0\xaf\xd0\x10T\xe21\x81\x07U5*\xf1\x98\x82HLv(%\xf3D?\x8f\x8ajT\xe21\x05\xf8\xf3X\xdd\x02\xa5\x94\xe4\x14n\xe5\x8d\xad\xfb\xab\x88\x84\x867\x8aj\x14OMb)\xa9F\xe7S\xd3\x90\x8c(\xc5S\x13y\xdc,;\xf6T\xe21\x8d\xeb\x97\x18\x8a\x0c\x08\x82 \x08\x82 \x08\x82 \x08\x82 \x08\x82 \x08\x82 \x08\x82 \x08\x82 \x08\x82 \x08\x82 \x08\x82 \x08\x82 \x08\xc2\xf8\x1f\xa8\xf8\xbd\xf8\x98\x8d^\x19\x00\x00\x00\x00IEND\xaeB`\x82')
            )

connection.commit()
connection.close()
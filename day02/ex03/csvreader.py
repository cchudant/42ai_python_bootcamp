class CsvReader():
    def __init__(self, path, sep=',', header=False, skip_top=0, skip_bottom=0):
        self.f = open(path, 'r')
        self.sep = sep
        self.header = header
        self.skip_top = skip_top
        self.skip_bottom = skip_bottom

    def __enter__(self):
        def perceval(v):
            v = v.strip()
            m = re.match(r'^"(.+)"$')
            if v.isnumeric():
                return int(v)
            elif m:
                return str(m[1])
            return None

        content = self.f.read()[self.skip_top:]
        if self.skip_bottom > 0:
            content = content[:self.skip_bottom]
        lines = content.split('\n')
        self.data = list(map(perceval, (ll.split(self.sep) for ll in lines)))

        ll = len(self.data[0])
        for line in self.data:
            if None in line or len(line) != ll:
                return None

        return self

    def __exit__(self):
        self.f.close()

    def getdata(self):
        if self.header:
            return self.data[1:]
        return self.data

    def getheader(self):
        if self.header:
            return self.data[1]
        raise ValueError('no header')


if __name__ == "__main__":
    with CsvReader('file.csv') as f:
        if f is None:
            print('file is corrupted')
        else:
            data = f.getdata()
            header = f.getheader()
            print(data, header)

import os
import os.path
import time
from datetime import datetime, timezone


def print_header(fh):
    header = """
<!doctype html>
<html>
<header>
<style>
    body {
        background-color: #BBCAFC;
    }
    div {
        margin: 3px;
        padding: 6px;
        border: 2px solid;
        font-size: 22px;
    }
    .even, div {
        color: black;
        background-color: white;
    }
    .odd, div {
        color: black;
        background-color: yellow;
    }
    .tiny {
        width: 20%;
    }
    .short {
        width: 30%;
    }
</style>
</header>
<body>
    """
    print(header, file=fh)


def print_footer(fh):
    footer = """
</body>
</html>
    """
    print(footer, file=fh)


def mk_link(root, node):
    return root + os.path.sep + node

def find_files(home, suffix = '.pdf', cap=None):
    results = dict()
    for root, dirs, nodes in os.walk(home):
        for node in nodes:
            if node.lower().endswith(suffix):
                file = mk_link(root, node)
                results[file] = os.stat(file).st_mtime
        if cap and len(results) > cap:
            break
    return results


def gen_report(suffix, home = os.getcwd()):
    results = find_files(home, suffix)

    if not results:
        print("None found.")
        quit()

    lres = sorted(results, key=lambda a: results[a], reverse=True)

    report = f"{suffix}_links.html"
    with open(report, "w") as fh:
        print_header(fh)
        print(f"<h1>{suffix.upper()} Links</h1>", file=fh)        
        print(f"<p>Reporting root is '{home}'</p>", file=fh)
        print(f"<p>Report generated @ {time.asctime()}</p>", file=fh)
        print("<table>", file=fh)
        for ss, file in enumerate(lres, 1):
            mtime = str(datetime.fromtimestamp(results[file])).split(':')[0:-1]
            mtime = mtime[0] + ':' + mtime[1]
            style = 'odd'
            if ss % 2 == 0:
                style = 'even'
            cols = file.split(os.path.sep)
            parent = cols[-2]
            dparent = 'file://'
            for z in cols[0:-1]:
                dparent += z + os.path.sep
            node = cols[-1]
            if len(node) > 45:
                node = node[:40] + f'... {suffix}'
            link = 'file://' + file
            print(f"<tr>\
                    <td><div class={style}>{ss:>04}.) <b>File: </b> {node} </div></td>\
                    <td class=tiny><div class={style}><b>Link: </b> <a href='{file}'>{mtime}</a></div></td>\
                    <td class=short><div class={style}><b>Folder: </b> <a href='{dparent}'>{parent}</a></div></td>\
                    </tr>", file=fh)
        print("</table>", file=fh)
        print_footer(fh)
    return report


if __name__ == '__main__':
    types = ".png", ".bmp", ".jpg", ".mp3", ".mp4", ".zip", ".pdf"
    for suffix in types:
        report = gen_report(suffix)
        os.popen(report)


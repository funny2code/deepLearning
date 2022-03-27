# -*- coding: utf-8 -*-
MNAME = "utilmy.template"
HELP = """ utils for """


import re
import os
from pprint import pprint



def get_file(file_path):
    """function _get_all_line
    Args:
        file_path:   
    Returns:
        
    """
    with open(file_path, 'r', encoding='utf-8') as f:
        all_lines = (f.readlines())
    return all_lines
    

def extrac_block(lines):
    """ Split the code source into Code Blocks:
        header
        import
        variable
        logger
        test
        core

        footer

    """
    dd = {}
    # lines = txt.split("/n")       
    lineblock = []

    flag_test= False

    ## BLOCK HEAD
    for ii,line in enumerate(lines) :
        # print(ii,line)
        # end of block header
        if (re.match(r"import\s+\w+", line) or \
            ((re.match(r"def\s+\w+", line) or re.match(r"class\s+\w+", line) or 'from utilmy import log' in line)) or \
                re.match(r'if __name__', line)) and ii < 20 :
            dd['header'] = lineblock
            dd['header_start_line'] = 0
            dd['header_end_line'] = ii - 1
            lineblock = []
            break
        else:
            lineblock.append(line)
            if ii >= 20:
                dd['header'] = []
                dd['header_start_line'] = 0
                dd['header_end_line'] = 0
                break
    # pprint(dd)
    lineblock = []
    
    # Block import
    dd['import_start_line'] = dd['header_end_line'] + 1 if dd['header_end_line'] else 0
    # print(dd['import_start_line'])
    for ii,line in enumerate(lines) :
        if ii >= dd['import_start_line']:
            # if ('def ' in line or 'class ' in line  or 'from utilmy import log' in line ) and ii < 50 and not 'import' in dd:
            if (re.match(r"def\s+\w+", line) or re.match(r"class\s+\w+", line) or 'from utilmy import log' in line or re.match(r'if __name__', line)) and ii < 50:
                dd['import'] = lineblock
                dd['import_end_line'] = ii - 1
                lineblock = []
                break
            else:
                # print(line)
                lineblock.append(line)
                if ii >= 50:
                    dd['import'] = []
                    dd['header_end_line'] = dd['header_start_line']
                    break
    # pprint(dd)
    lineblock = []

    ### Block Logger
    dd['logger_start_line'] = dd['import_end_line'] + 1 if dd['import_end_line'] else 0
    for ii,line in enumerate(lines) :
        if ii >= dd['logger_start_line']:
            if (re.match(r"def\s+\w+", line)) and ii < 50:
                if not('def help' in line or 'def log' in line):
                    dd['logger'] = lineblock
                    dd['logger_end_line'] = ii - 1
                    lineblock = []
                    break
                else:
                    lineblock.append(line)
            else:
                # print(line)
                lineblock.append(line)
                if ii >= 50:
                    dd['logger'] = []
                    dd['logger_end_line'] = dd['logger_start_line']
                    break
    # pprint(dd)
    lineblock = []

    ### Block Test
    dd['test_start_line'] = dd['logger_end_line'] + 1 if dd['logger_end_line'] else 0
    for ii,line in enumerate(lines) :
        if ii >= dd['test_start_line']:
            # new function / class / or main
            if (re.match(r"def\s+\w+", line) or \
                 re.match(r"class\s+\w+", line)) or \
                 re.match(r'if __name__', line):
                if not('def test' in line):
                    dd['test'] = lineblock
                    dd['test_end_line'] = ii - 1
                    lineblock = []
                    break
                else:
                    lineblock.append(line)
            else:
                # print(line)
                lineblock.append(line)
                if ii == len(lines)-1:
                    dd['test'] = []
                    dd['test_end_line'] = dd['test_start_line']
                    break
    # pprint(dd)

    lineblock = []

    # Block Core
    dd['core_start_line'] = dd['test_end_line'] + 1 if dd['test_end_line'] else 0
    for ii,line in enumerate(lines) :
        if ii >= dd['core_start_line']:
            # new function / class / or main
            if re.match(r'if __name__', line):
                # print('----------------')
                dd['core'] = lineblock
                dd['core_end_line'] = ii - 1
                lineblock = []
                break
            else:
                # print(line)
                lineblock.append(line)
                if ii == len(lines)-1:
                    dd['core'] = []
                    dd['core_end_line'] = dd['core_start_line']
                    break
    # pprint(dd)

    lineblock = []
    dd['footer_start_line'] = dd['core_end_line'] + 1 if dd['core_end_line'] else 0
    for ii,line in enumerate(lines):
        if ii >= dd['footer_start_line']:
            lineblock.append(line)
        if ii == len(lines) -1:
            dd['footer'] = lineblock
            dd['footer_end_line'] = ii
            break
    # pprint(dd)

    return dd


def normalize_header(file_name, lines):
    """Nomarlize Header block

    Args input is a array of lines.
    """
    #### not need of regex, code easier to read 

    lines2 = []
    if len(lines) >= 3:
        # line 1
        if '# -*- coding: utf-8 -*-' not  in lines[0] :
            lines2.append('# -*- coding: utf-8 -*-\n')

        # line 2
        if 'MNAME' not in lines[1] :   ### MNAME = "utilmy.docs.format"
            nmane =  ".".join( os.path.abspath(file_name).split("\\")[-4:] )[:-3]
            lines2.append( f'MNAME = "{nmane}"\n')

        if 'HELP' not in lines[2] :   ### HELP
            lines2.append( f'HELP = "util"\n')

    else:
        lines2.append('# -*- coding: utf-8 -*-\n')
        nmane =  ".".join( os.path.abspath(file_name).split("\\")[-4:] )[:-3]
        lines2.append( f'MNAME = "{nmane}"\n')
        lines2.append( f'HELP = "util"\n')

    ### Add previous line
    lines2.extend(lines)
    # print(lines2)
    return lines2


def normalize_import(lines):
    """  merge all import in one line and append others

    """
    import_list = []
    from_list = []
    lines2 = []
    for line in lines :
        if "import " in line :
            if "from " in line : from_list.append(line)
            else :               import_list.append(line)

    ### Merge all import in one line   ################################################
    llall = []
    for imp in import_list :
        imp = imp[6:] # remove import
        ll    = [ t.strip() for t in  imp.split(",") if 'import' not in t ]
        llall = llall + ll

    lall = sorted( llall )

    lines2 = []
    ss = "import "
    for mi in lall:
        ss =  ss + mi + ", "
        if len(ss) >  90 :
            lines2.append( f"{ss[:-2]}\n" )  
            ss = "import "
    lines2.append(f"{ss[:-2]}\n")  

    # lines2.extend(from_list)
    # print(lines2)

    #### Remaining import 
    for ii, line in enumerate(lines):
        if ii > 100 : break
        if line.startswith("import ") : continue  ### Remove Old import
        lines2.append(line)  

    #### 
    # print(lines2)
    return lines2




def normalize_logger(lines):
    lines2 = []
    if len(lines) >0:
        if "from utilmy import log" not in lines[0]:
            lines2.append('from utilmy import log, log2, help_create\n')
    else:
        lines2.append('from utilmy import log, log2, help_create\n')
    # append all
    lines2.extend(lines)

    # check help function:
    is_exist_help = False
    for line in lines:
        if line.startswith("def help"):
            is_exist_help = True
            break
    
    if not is_exist_help:
        lines2.extend([
            'def help():\n',
            '   print( HELP + help_create(MNAME) )\n',
            '\n',
            '\n'
        ])
    # print(lines2)
    return lines2


def normalize_test(lines):
    lines2 = []

    # check test_all function:
    is_exist_test_all = False
    for line in lines:
        if line.startswith("def test_all"):
            is_exist_test_all = True
            break
    
    if not is_exist_test_all:
        lines2.extend([
            'def test_all() -> None:\n',
            '    """function test_all"""\n',
            '    log(MNAME)\n',
            '    test1()\n',
            '    test2()\n',
            '\n',
            '\n',
        ])

    # check test1 function:
    is_exist_test1 = False
    for line in lines:
        if line.startswith("def test1"):
            is_exist_test1 = True
            break
    
    if not is_exist_test1:
        lines2.extend([
            'def test1() -> None:\n',
            '    """function test"""\n',
            '    pass\n',
            '\n',
            '\n',
        ])

    """  
    # check test2 function:
    is_exist_test2 = False
    for line in lines:
        if line.startswith("def test2"):
            is_exist_test2 = True
            break
    
    if not is_exist_test2:
        lines2.extend([
            'def test2() -> None:\n',
            '    """function test"""\n',
            '    pass\n',
            '\n',
            '\n',
        ])
    """

    ###### Eztend lines
    lines2.extend(lines)
    return lines2

def normalize_core(lines):
    return lines


def normalize_footer(lines):

    txt = "\n".join(lines)

    if "if __name__" not in txt: lines2.append( 'if __name__ == "__main__":' )
    if "import fire" not in txt:  lines2.append( '  import fire' )
    if "import fire" not in txt:  lines2.append( '  fire.Fire()' )

    lines2 = lines2 + lines

    return lines2





def read_and_normalize_file(file_path, output_file):
    all_lines = get_file(file_path)
    info = extrac_block(all_lines)

    new_headers = normalize_header(file_path, info['header'])
    new_imports = normalize_import(info['import'])
    new_loggers = normalize_logger(info['logger'])
    new_tests =   normalize_test(info['test'])
    new_cores =   normalize_core(info['core'])
    new_footers = normalize_footer(info['footer'])

    # Create new data array then write to new file
    new_all_lines = []
    new_all_lines.extend(new_headers)
    new_all_lines.extend(new_imports)
    new_all_lines.extend(new_loggers)
    new_all_lines.extend(new_tests)
    new_all_lines.extend(new_cores)
    new_all_lines.extend(new_footers)

    with open(output_file, 'w+', encoding='utf-8') as f:
        f.writelines(new_all_lines)


if __name__ == '__main__':
    read_and_normalize_file('test_script/test_script_no_header.py', 'test_script/output/test_script_no_header.py')
    read_and_normalize_file('test_script/test_script_no_logger.py', 'test_script/output/test_script_no_logger.py')
    read_and_normalize_file('test_script/test_script_no_core.py', 'test_script/output/test_script_no_core.py')
    read_and_normalize_file('test_script/test_script_normalize_import.py', 'test_script/output/test_script_normalize_import.py')


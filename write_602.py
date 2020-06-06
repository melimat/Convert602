def write_to_602(text_to_write, filename):
    ct_int = 1 #unknown purpose
    lm_int = 1 #left margin
    rm_int = 65 #right margin
    pl_int = 55 #page length
    mt_int = 3 #top margin
    mb_int = 3 #bottom margin
    po_int = 5 #print from column
    pn_int = 1 #print from page number
    lh_int = 4 #unknown purpose

    ct_str = "@CT " + str(ct_int)
    lm_str = "@LM " + str(lm_int)
    rm_str = "@RM " + str(rm_int)
    pl_str = "@PL " + str(pl_int)
    tb_str = "@TB " + "-----T"*22
    mt_str = "@MT " + str(mt_int)
    mb_str = "@MB " + str(mt_int)
    po_str = "@PO " + str(po_int)
    pn_str = "@PN " + str(pn_int)
    lh_str = "@LH " + str(lh_int)


    config_head_list = [ct_str, lm_str, rm_str, pl_str, tb_str, mt_str, mb_str, po_str, pn_str, lh_str]
    config_head_str = "\r\n".join(config_head_list) + "\r\n"

    with open(filename, mode="wb") as output_file:
        output_file.write(config_head_str.encode("cp852"))
        output_file.write(text_to_write.encode("cp852", "ignore"))
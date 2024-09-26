interface ISiteMetadataResult {
  siteTitle: string;
  siteUrl: string;
  description: string;
  logo: string;
  navLinks: {
    name: string;
    url: string;
  }[];
}

const data: ISiteMetadataResult = {
  siteTitle: 'Timhai Running Page',
  siteUrl: 'https://timhaiz.github.io/running_page/',
  logo: 'https://www.logosc.cn/uploads/icon/2021/09/16/42bf786b-d617-478f-a36a-a063c3b1c9e2.png',
  description: 'Personal site and blog',
  navLinks: [

    {
      name: 'About',
      url: 'https://github.com/yihong0618/running_page/blob/master/README-CN.md',
    },
  ],
};

export default data;

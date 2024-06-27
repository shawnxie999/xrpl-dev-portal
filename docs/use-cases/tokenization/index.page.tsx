import React, { useRef, useState } from "react";
import { useTranslate } from "@portal/hooks";
import { NavList } from "shared/components/nav-list";
import { Link } from '@portal/Link';

const { translate } = useTranslate();

export const frontmatter = {
  seo: {
    title: "Tokenization",
    description:
      "Explore the possibilities of tokenization on the XRP Ledger, revolutionizing ownership, transactions, and value exchange with unparalleled efficiency and security.",
  },
};

const useCases = [
  {
    description: "Stablecoin Issuer",
    link: "/docs/use-cases/tokenization/stablecoin-issuer/",
  },
  {
    description: "NFT Marketplace",
    link: "/docs/use-cases/tokenization/nftoken-marketplace/",
  },
  {
    description: "Authorized Minter",
    link: "/docs/use-cases/tokenization/authorized-minter/",
  },
  {
    description: "Digital Artist",
    link: "/docs/use-cases/tokenization/digital-artist/",
  },
];

const securityAdvantages = [
  {
    id: "trustlines",
    title: "Trust Lines & Authorized Trust Lines",
    description: (
      <>
        <Link to="/docs/concepts/tokens/fungible-tokens/"><h5 className="card-subhead">{translate("Trust Lines:")}</h5></Link>
        <div className="card-text">
          {translate("No spamming of wallets without permission.")}
        </div>
        <Link to="/docs/concepts/tokens/fungible-tokens/authorized-trust-lines/"><h5 className="card-subhead">{translate("Authorized Trustlines:")}</h5></Link>
        <div className="card-text">
          {translate(
            "Control who can hold your tokens with allowlisting."
          )}
        </div>
      </>
    ),
  },
  {
    id: "freeze-clawbacks",
    title: "Freeze & Clawbacks",
    description: (
      <>
        <Link to="/docs/concepts/tokens/fungible-tokens/"><h5 className="card-subhead">{translate("Freeze:")}</h5></Link>
        <div className="card-text">
          {translate(
            "If you see signs of suspicious activity, you can suspend trading of your token while investigating the issue."
          )}
        </div>
        <Link to="/docs/concepts/tokens/fungible-tokens/clawing-back-tokens/"><h5 className="card-subhead">{translate("Clawback:")}</h5></Link>
        <div className="card-text">
          {translate(
            "Recover tokens distributed to accounts in error: for example, reclaim funds sent to an account sanctioned for illegal activity."
          )}
        </div>
      </>
    ),
  },
  {
    id: "ntf-tokens",
    title: "Non-transferable Tokens",
    description: (
      <>
        <Link to="/docs/concepts/tokens/nfts/non-transferable-tokens/"><h5 className="card-subhead">{translate("Transferable flag:")}</h5></Link>
        {translate(
          "Native support for nontransferable items such as identity tokens, airline credits, and consumer rewards, honored by all on-chain participants."
        )}
      </>
    ),
  },
  {
    id: "royalties",
    title: "Royalties",
    subtitle: "Secures Creator Compensation:",
    description: (
      <>
        <Link to="/docs/references/protocol/data-types/nftoken/#transferfee"><h5 className="card-subhead">{translate("NFT Transfer Fees:")}</h5></Link>
        {translate(
          "Reliably collect your percentage of the sale price of your tokens."
        )}
      </>
    ),
  },
];

const stats = [
  {
    id: "nfts-minted",
    stat: "20K",
    description: "NFTs minted",
  },
  {
    id: "nft-trading-vol",
    stat: "~1000",
    description: "NFT trading volume",
  },
  {
    id: "network-speed",
    stat: "0.4",
    description: "Network speed (sec)",
  },
  {
    id: "fee-per-tx",
    stat: "$0.001",
    description: "Avg fee per NFT tx",
  },
];

const projects = [
  {
    id: "xrpcafe",
    label: "XRP cafe",
    url: "https://xrp.cafe",
  },
  {
    id: "onXRP",
    label: "onXRP",
    url: "https://nft.onxrp.com",
  },
  {
    id: "xaman",
    label: "Xaman labs",
    url: "https://github.com/XRPL-Labs/Xaman-App",
  },
  {
    id: "amy",
    label: "amy.network",
    url: "https://token.amy.network",
  },
  {
    id: "sologenic",
    label: "Sologenic",
    url: "https://sologenic.org/trade",
  },
  {
    id: "carbonland",
    label: "Carbonland trust",
    url: "https://www.carbonlandtrust.com",
  },
  {
    id: "nautilus",
    label: "Nautilus wallet",
    url: "https://github.com/nautls/nautilus-wallet",
  },
  {
    id: "evernode",
    label: "Evernode",
    url: "https://evernode.org",
  },
  {
    id: "raised-in-space",
    label: "Raised in space",
    url: "https://raisedinspace.com",
  },
];

const articles = [
  {
    time: "JAN 2024",
    title: "XRP Price Prediction: Will Ripple Make Waves in 2024?",
    url: "https://www.forbes.com/advisor/au/investing/cryptocurrency/xrp-price-prediction",
  },
  {
    time: "JAN 2024",
    title: "XRP Could Surge Massively in 2024",
    url: "https://u.today/xrp-could-surge-massively-at-beginning-of-2024-heres-why",
  },
  {
    time: "NOV 2023",
    title: "NFTs and the XRPL: A Marriage of Art and Technology",
    url: "https://medium.com/@MariaSolorzano/title-nfts-and-the-xrpl-a-marriage-of-art-and-technology-cf76a0432693",
  },
];

const FeaturedProjects = () => {
  const [currentIndex, setCurrentIndex] = useState(0);

  const handlePrev = () => {
    if (currentIndex > 0) {
      setCurrentIndex(currentIndex - 1);
    }
  };

  const handleNext = () => {
    if (currentIndex < projects.length - 3) {
      setCurrentIndex(currentIndex + 1);
    }
  };

  const ProjectCard = ({ project, index }) => (
    <a
      className={`col card float-up-on-hover ${
        index % 2 === 0 ? "even" : "odd"
      }`}
      target="_blank"
      href={project.url}
    >
      <div className="project-logo d-flex justify-content-center align-items-center mb-8">
        <img className={project.id} alt={project.label} />
      </div>
      <div className="project-name h5 align-self-center">{project.label}</div>
    </a>
  );

  return (
    <div className="featured-projects">
      <div className="project-cards-container card-grid card-grid-3xN">
        <ProjectCard project={projects[currentIndex]} index={currentIndex} />
        <ProjectCard
          project={projects[currentIndex + 1]}
          index={currentIndex + 1}
        />
        <ProjectCard
          project={projects[currentIndex + 2]}
          index={currentIndex + 2}
        />
      </div>
      <div className="arrow-wrapper d-flex justify-content-center mt-16">
        <button
          className={`arrow-button prev ${
            currentIndex > 0 ? "hover-color" : ""
          }`}
          onClick={handlePrev}
        >
          <img alt="left arrow" />
        </button>
        <button
          className={`arrow-button next ${
            currentIndex < projects.length - 3 ? "hover-color" : ""
          }`}
          onClick={handleNext}
        >
          <img alt="right arrow" />
        </button>
      </div>
    </div>
  );
};

export default function Tokenization() {
  const modalRef = useRef(null);

  return (
    <div className="landing page-tokenization">
      <div className="position-relative"></div>
      <div className="position-relative d-none-sm"></div>
      <section className="container-new mt-lg-16">
        <div className="card-grid card-grid-2xN">
          <div className="col">
            <img className="tokenization-graphic mw-100 hide-md" />
          </div>
          <div className="col">
            <div className="d-flex flex-column-reverse">
              <img className="tokenization-graphic mw-100 show-md" />
              <h2 className="h4 h2-sm mb-10">
                {translate(
                  "Work with a variety of tokens supported by the XRP Ledger."
                )}
              </h2>
              <h6 className="eyebrow mb-3 text-large">
                {translate("Tokenization")}
              </h6>
            </div>
            <p className="mb-10">
              {translate(
                "Explore the possibilities of tokenization on the XRP Ledger, revolutionizing ownership, transactions, and value exchange with unparalleled efficiency and security."
              )}
            </p>
            <div className="tokenization-color-bar" />
            <div className="mb-10">
              <NavList pages={useCases} bottomBorder={false} />
            </div>
            <div className="d-flex">
              <a
                className="btn btn-primary d-inline-flex align-items-center"
                href="/docs"
              >
                {translate("Quick Start")}
              </a>{" "}
              <a
                className="ml-4 video-external-link btn-none"
                target="_blank"
                href="https://www.youtube.com/playlist?list=PLJQ55Tj1hIVZtJ_JdTvSum2qMTsedWkNi"
              >
                <i className="fa fa-video-camera" />
                <span className="link-text">{translate("Learn more")}</span>
              </a>
            </div>
          </div>
        </div>
      </section>
      <section className="container-new py-20">
        <div className="d-flex flex-column-reverse">
          <p className="mb-16">
            {translate(
              "Check out the security features you can tap into right from the chain without the hassle of piecing together smart contracts."
            )}
          </p>
          <h4 className="eyebrow mb-8">{translate("Security advantages")}</h4>
        </div>
        <div
          className="security-card-grid nav card-grid"
          id="security-features"
        >
          {securityAdvantages.map((advantage) => (
            <div className="security-card" key={advantage.id}>
              <div className="card-body p-6">
                <h4 className="card-title h6">{translate(advantage.title)}</h4>
                <div>{advantage.description}</div>
              </div>
            </div>
          ))}
        </div>
      </section>

      <section className="container-new py-20">
        <div className="d-flex flex-column-reverse">
          <h4 className="eyebrow mb-16">{translate("Stats")}</h4>
        </div>
        <div className="tokenization-stats">
          {stats.map((statElement) => (
            <div
              className="stat-container align-items-center"
              key={statElement.id}
            >
              <div className="stat">{statElement.stat}</div>
              <div className="desc">{translate(statElement.description)}</div>
            </div>
          ))}
        </div>
      </section>
      <section className="container-new py-20">
        <div className="d-flex flex-column-reverse">
          <h4 className="eyebrow mb-16">
            {translate("Featured real world projects")}
          </h4>
        </div>
        <div className="project-cards">
          <FeaturedProjects />
        </div>
      </section>

      <section className="container-new py-20">
        <div className="d-flex flex-column-reverse">
          <h4 className="eyebrow mb-16">{translate("Related Articles")}</h4>
        </div>
        <div className="related-articles card-grid card-grid-3xN mb-16">
          {articles.map((article, index) => (
            <div className="article-card-container" key={`article-${index}`}>
              <div className="article-card-background" />
              <a
                className="article-card col p-8 float-up-on-hover"
                target="_blank"
                href={article.url}
              >
                <div className="time h4 normal mb-8">
                  {translate(article.time)}
                </div>
                <div className="h5 mb-4">{translate(article.title)}</div>
                <div className="btn btn-primary btn-arrow-out">
                  {translate("Read More")}
                </div>
              </a>
            </div>
          ))}
        </div>
        <div className="more-related">
          <div className="d-flex flex-column-reverse">
            <h4 className="eyebrow mb-16">
              {translate("More related articles")}
            </h4>
          </div>
          <div className="video-external-link">
            <a href="https://coincodecap.com/ripple-xrp">
              {translate(
                "Ripple (XRP): A Dive into its Working, Tokenomics, Price Factor and SEC Lawsuit"
              )}
            </a>
          </div>
          <div className="subtitle">{translate("November 2023")}</div>
        </div>
      </section>
    </div>
  );
}

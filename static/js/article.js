const tickerAmount = 3;

const tickerElemHTML = t => `
<div class="ticker-row">
  <span class="image-wrap">
      <img src="https://pbs.twimg.com/profile_images/563716194323025921/OthWJnik_400x400.png" class="img-responsive" alt="">
    </span>
      
      <div class="ticker-text-wrap">
        <h3>${t["CompanyName"]}</h3>
        <h4>
            <span class="ticker">
                <a title="${t["CompanyName"]} Stock Quote" href="#">
                    NASDAQ:<span class="symbol">${t["Symbol"]}</span>
                </a>
            </span>
        </h4>
      <aside class="price-quote-container">
          <h4 class="current-price">
            $${t["CurrentPrice"]["Amount"]}
          </h4>
          <h4 class="price-change-amount ${
            t["Change"]["Amount"] >= 0 ? "price-pos" : "price-neg"
          }">
              &nbsp; $${Math.abs(t["Change"]["Amount"])}
          </h4>
          <h4 class="price-change-percent ${
            t["PercentChange"]["Value"] >= 0 ? "price-pos" : "price-neg"
          }"">
          &nbsp; ( ${Math.abs(
            Math.round(t["PercentChange"]["Value"] * 100) / 100
          )}% )
          </h4>
      </aside>
    </div>
</div>`;

const updateTickerContainer = tickersHTMLElems => {
  let container = $("#tickers-container");
  container.empty();
  tickersHTMLElems.forEach(t => {
    container.append(t);
  });
};

const loadTickers = () => {
  $.ajax({
    url: `${window.location.href}tickers/${tickerAmount}`
  }).done(({ newTickers }) => {
    const tickersHTMLElems = newTickers.map(tickerElemHTML);

    updateTickerContainer(tickersHTMLElems);
  });
};

$(document).ready(function() {
  loadTickers();

  $(".add-comment-icon").click(e => {
    $(".comment-add-section").addClass("display-flex");
  });

  $("#ticker-refresh-btn").click(loadTickers);
  $(".markdown-content").each(function() {
    let contentToMarkdown = $(this).html();

    let markeddownContent = marked(contentToMarkdown);

    $(this).html(markeddownContent);
  });
});
